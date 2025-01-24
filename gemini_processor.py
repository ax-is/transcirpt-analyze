
import google.generativeai as genai

class GeminiProcessor:
    def __init__(self):
        genai.configure(api_key="AIzaSyAOipTAG6P0x4raWrMWlYjaAn_6vfBBOc4")
        self.model = genai.GenerativeModel("gemini-1.5-flash")

   

    async def getAnalytics(self, transcript: str, prompt: str):
        try:
            response = self.model.generate_content(f"{prompt}\n\nChatbot Transcript: {transcript}")
            # Generate analytics for each header in the prompt
            analytics = {}
            for line in prompt.split("\n"):
                header = line.split(":")[0]
                analytics[header] = response.text.strip().split("\n")[0]
            return {"analytics": analytics}
        except Exception as e:
            return {"error": f"Failed to generate analytics: {str(e)}"}
