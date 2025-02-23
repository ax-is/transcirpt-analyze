import google.generativeai as genai
from services.base import GenAIParent
import json

class Gemini(GenAIParent):
    service_name = "Gemini"

    def __init__(self):
        genai.configure(api_key="YOUR API KEY")
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    async def getAnalytics(self, transcript: str, prompt: str):
        try:
            # Generate the response from the LLM in JSON format
            response = self.model.generate_content(
                f"{prompt}\n\nChatbot Transcript: {transcript}",
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json"  
                )
            )

            print("Raw LLM Response:", response.text)

            try:
                analytics = json.loads(response.text)
            except json.JSONDecodeError:
                return {"error": "Failed to parse Gemini response as JSON."}

            return analytics

        except Exception as e:
            return {"error": f"Gemini failed to generate analytics: {str(e)}"}