import google.generativeai as genai
from services.base import GenAIParent
import json

class test(GenAIParent):
    service_name = "test"

    def __init__(self):
        genai.configure(api_key="AIzaSyAPknYECJz-CQBJ530ofC0CpSnyMnFwGSk")
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