from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os
import logging
import asyncio
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Configure the API key
GOOGLE_API_KEY = "AIzaSyDtl4DdV6-zDQ-G5yTRKS9dFYchfZeuVKk"
genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str, websocket: WebSocket):
        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_text(message)

manager = ConnectionManager()

# Initialize the model
generation_config = {
    "temperature": 0.2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
)

chat_session = model.start_chat(history=[])

async def process_text(text: str, mode: str) -> str:
    try:
        logger.debug(f"Processing text in {mode} mode: '{text}'")
        if mode == 'filter':
            prompt = f"""
             Act as a strict content moderator. Analyze and clean the following text:

            Text to analyze: '{text}'

            Content Filtering Rules:
            1. Remove any profanity or explicitly offensive words (don't replace with symbols, just remove them)
            2. Remove any slurs or hate speech completely
            3. Remove any explicit adult content references
            4. Keep all other words exactly as they are
            5. Maintain spaces between remaining words
            6. If a sentence becomes grammatically incorrect after removal, fix only the essential grammar
            7. DO NOT add any new words or explanations
            8. DO NOT modify non-offensive casual language
            9. Return ONLY the cleaned text

            Return the filtered text:
            """
        else:  # professional mode
            prompt = f"""
            You are a professional language enhancer. Your task is to modify the input text to make it more professional and kind, while preserving its core meaning. Here is the text:

            '{text}'

            Rules:
            1. Improve the language to be more professional and courteous.
            2. Maintain the original meaning and intent of the message.
            3. Remove any offensive language or inappropriate content.
            4. Do NOT add any explanations or comments.
            5. Keep the length of the text similar to the original.

            Return ONLY the modified text:
            """
        
        response = await asyncio.to_thread(chat_session.send_message, prompt)
        processed_text = response.text.strip()
        logger.debug(f"Processed text: '{processed_text}'")
        return processed_text
    except Exception as e:
        logger.error(f"Error in process_text: {e}")
        return text  # Return original text if there's an error

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            text = message_data['text']
            mode = message_data['mode']
            logger.info(f"Received message from client #{client_id}: '{text}' (Mode: {mode})")
            
            # Process the message
            processed_text = await process_text(text, mode)
            logger.info(f"Processed message for client #{client_id}: '{processed_text}'")
            
            # Send the original message back to the sender for immediate feedback
            await manager.send_personal_message(f"You: {text}", websocket)
            
            
            if processed_text != text:
                await manager.send_personal_message(f"Your message was modified to: {processed_text}", websocket)
            
            # Broadcast the processed message to other clients
            await manager.broadcast(f"Client #{client_id}: {processed_text}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

# Serve the HTML file
@app.get("/")
async def get():
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)