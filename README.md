<div align="center">
  <h1><b>EmpathyChat: AI Based Content Filtering ✨</b></h1>
  <img src="https://github.com/user-attachments/assets/aabb3ec1-a78e-4bbb-9460-e18b611b9092" width="300"/>
</div>

## Introduction 🌍

In an increasingly digital world, the way we communicate shapes our relationships and influences how we receive feedback. To address the growing need for more empathetic and constructive communication, we have developed a real-time chat app that transforms the way users express themselves in reviews and feedback scenarios. 

This innovative app tweaks users' words into a more professional and compassionate tone, encouraging thoughtful and respectful exchanges. By facilitating empathetic communication, our app aims to enhance the quality of online interactions, whether in restaurant reviews 🍴, product feedback 📦, or constructive critiques 💬, ultimately fostering a culture of understanding and support.

## Objectives 🎯

- Develop a real-time chat application using WebSockets, allowing multiple users to communicate seamlessly.
- Implement advanced features for filtering out vulgar words 🚫 without removing the comment entirely.
- Converting negative sentiments into positive expressions, thereby promoting a healthier communication environment 🌱.
  

## Web Sockets 🌐

WebSocket is bidirectional, a full-duplex protocol used in the same client-server communication scenario as HTTP, but it starts with `ws://` or `wss://`. It is a stateful protocol, meaning the connection between the client and server remains open until terminated by either party. 

In real-time web applications, WebSockets allow for continuous communication between the client and the server. For example, when Client A sends a message, it is immediately visible to Client B.

WebSockets are used to filter and modify messages in real-time. When a client sends a message containing inappropriate content, the server intercepts and filters it before broadcasting the modified message.

## Methodology 🛠️

<div align="center">
  <img src="https://github.com/user-attachments/assets/8ac4efb6-95aa-409e-9a20-93a9c3f53bd4" width="600"/>
</div>

Tech stack:

1. **Backend**: Python FastAPI, WebSocket for real-time communication.
2. **Frontend**: HTML/CSS and JavaScript.
3. **AI**: Uses AI-driven filtering to transform negative tones into positive and professional responses via Google Generative AI 
4. **Deployment**: The application is deployed using Docker as a microservice.



## Results & Discussions 📝
### Without Pro mode 🚫:

<table align="center">
  <tr>
    <td align="center"><b>Sender Client</b></td>
    <td align="center"><b>Receiver Client</b></td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/a2049ec7-ca95-4b23-9ad6-b2df543a40bd" width="300"/>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/a3cc6074-915c-447c-b446-53db345e1f17" width="300"/>
    </td>
  </tr>
</table>

<br/>

### Pro Mode 🌟:

 - **Choice of enabling Pro mode is up to the sender, allowing them to choose whether to enable the feature or not.**
 - **This is not to restrict free speech, but rather an option for more professional communication.**
 - **As the choice is in your hands, the data security is also not an issue as we are only sending the data to ai model when its in pro mode**

<table align="center">
  <tr>
    <td align="center"><b>Sender Client (With Pro mode Enabled)</b></td>
    <td align="center"><b>Receiver Client</b></td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/fccc42cc-fe31-41c7-898d-e746beeccf2c" width="300"/>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/6bc4f16b-759e-46d6-b906-4d7468a17a43" width="300"/>
    </td>
  </tr>
</table>



## Conclusion 🏁

In this digital age, communication shapes relationships and feedback. Our real-time chat app facilitates empathetic and constructive communication by transforming negative expressions into professional tones. This innovation promotes understanding, support, and respect in online interactions.

## Literature Survey 📚

| Authors| Summary |
| ----- | ------- |
| Davidson, T., Warmsley, D., Macy, M., & Weber, I. (2017) | This paper explores challenges in differentiating hate speech from offensive language using NLP approaches and various classifiers. |
| Fortuna, P., & Nunes, S. (2018) | The study surveys different methods and challenges in detecting hate speech using computational models. |
| Saleh, H., Alhothali, A., & Moria, K. (2021) | This paper investigates the use of BERT and domain-specific word embeddings for detecting hate speech with a high F1 score. |
| Zhou, X., & Zafarani, R. (2018) | A comprehensive survey that discusses the complexities of hate speech detection on platforms like Twitter and Facebook. |
| Mathew, B., Saha, P., Yimam, S. M., Biemann, C., Goyal, P., & Mukherjee, A. (2021) | Focuses on creating datasets that aid in making hate speech detection models more interpretable. |
| Schmidt, A., & Wiegand, M. (2017) | Discusses NLP-based methods for detecting hate speech across various languages and datasets. |
| Wang, Z., Hale, S. A., Adelani, D. I., Grabowicz, P., Hartman, T., Floeck, F., & Jurgens, D. (2020) | Examines the relationship between demographics and the prevalence of hate speech across social media. |
| Badjatiya, P., Gupta, S., Gupta, M., & Varma, V. (2017) | Introduces deep learning techniques for identifying hate speech on Twitter. |
| Mubarak, H., Darwish, K., & Magdy, W. (2017) | Focuses on the detection of hate speech and abusive language in Arabic, providing insights into multilingual challenges. |

## Steps for Running the Application 🚀

1. Clone the repository.
2. Navigate to the project directory.
- put the index.html in templates folder(i forgot to add it)
- replace the gemini api key
- check gemini version
- (only runs with this) 
3. Run the backend with the following command:
python -m uvicorn app:app --reload



