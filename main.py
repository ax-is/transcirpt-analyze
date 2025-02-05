from fastapi import FastAPI, HTTPException
from services.base import GenAIParent
from services.gemini import Gemini 
from schemas import ServiceEnum, TranscriptAnalysisRequest

app = FastAPI()

@app.post("/analyze-transcript/")
async def analyze_transcript(Service: ServiceEnum, payload: TranscriptAnalysisRequest):
    try:
        # Get the service class dynamically based on the selected service
        service_class = GenAIParent.get_service_class(Service)
        ai_processor = service_class()
        
        # Combine headers and descriptions into a prompt
        combined_headers = [
            f"{header.header}: {header.description}"
            for header in payload.headers
        ]
        combined_prompt = "\n".join(combined_headers)

        # Generate analysis
        llm_response = await ai_processor.getAnalytics(
            transcript=str(payload.transcript),
            prompt=(
                "Please analyze in one sentence the following transcript using the fields below (only give analysis for provided fields). "
                "Each field should have a corresponding analysis in the JSON schema:\n"
                "'Field Name' : 'Analysis Result'.\n\n"
                f"{combined_prompt}\n\nTranscript: {payload.transcript}"
            )
        )

        return llm_response

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")