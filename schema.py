from pydantic import BaseModel  
from typing import List, Dict

class HeaderDescription(BaseModel):
    header: str
    description: str

class TranscriptAnalysisRequest(BaseModel):
    headers: List[HeaderDescription]
    transcript: List[Dict[str, str]]
