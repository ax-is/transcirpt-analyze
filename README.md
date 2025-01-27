# Transcript Analysis API

A FastAPI-based application that uses Gemini's generative AI model to analyze chatbot transcripts with customizable headers and descriptions. Designed for developers seeking AI-powered transcript insights.

---

## 🚀 Features
- **Custom Headers**: Define headers and descriptions to tailor analysis.
- **AI-Powered Analysis**: Leverages Gemini's generative AI for concise and insightful responses.
- **RESTful API**: Easily integrate the service with other systems.
- **Modular Structure**: Designed for scalability and ease of maintenance.

---

## 📂 Project Structure

```
transcript-analysis-api/
├── main.py                # FastAPI app and endpoint definitions
├── gemini_processor.py    # Handles interaction with Gemini AI
├── schema.py              # Pydantic models for request validation
├── service_manager.py     # Business logic and service coordination
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
└── .gitignore             # Ignored files in version control
```

---

## ⚙️ Setup Instructions

### Prerequisites
- **Python Version**: Python 3.9 or higher
- **Gemini API**: Google Generative AI SDK (`google.generativeai`)
- **API Key**: A valid Gemini API key

---

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/transcript-analysis-api.git
   cd transcript-analysis-api
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key**:
   - Open `gemini_processor.py` and replace the placeholder `AIzaSyAOipTAG6P...` with your **Gemini API key**.

---

### Run the Application

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access API Documentation**:
   - Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## 📬 API Endpoints

### 1. **Analyze Transcript**

- **URL**: `/analyze-transcript/`  
- **Method**: `POST`  
- **Description**: Analyzes a chatbot transcript based on the headers and descriptions provided.

**Request Body Example**:
```json
{
  "headers": [
    { "header": "Customer Sentiment", "description": "Insights on customer feelings and tone" },
    { "header": "Agent Behavior", "description": "Evaluation of agent's professionalism" }
  ],
  "transcript": [
    { "speaker": "Customer", "message": "This was fantastic!" },
    { "speaker": "Agent", "message": "Thank you! Happy to help!" }
  ]
}
```

**Response Example**:
```json
{
  "Customer Sentiment": "Positive sentiment detected.",
  "Agent Behavior": "Agent maintained professionalism."
}
```

---

## 🛠️ Built With
- **[FastAPI](https://fastapi.tiangolo.com/)**: For building the RESTful API.
- **[Google Generative AI](https://cloud.google.com/generative-ai/)**: Used for transcript analysis.
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Data validation and settings management.

---

## 📝 License
This project is licensed under the [MIT License](LICENSE).

---

## 💡 Future Enhancements
- Add authentication and role-based access control.
- Implement detailed error handling and logging mechanisms.
- Extend to support multiple AI models and other languages.

---

This version is now back to using bullet points (`*`) for GitHub compatibility! Let me know if you need anything else. 😊
