from fastapi import FastAPI, HTTPException
from service_manager import transcript_analyze
from schema import TranscriptAnalysisRequest  

app = FastAPI()

@app.post("/analyze-transcript/")
async def analyze_transcript(payload: TranscriptAnalysisRequest):
    try:
        result = await transcript_analyze(payload)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
