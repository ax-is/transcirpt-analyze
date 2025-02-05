from pydantic import BaseModel
from typing import List, Dict
from enum import Enum


class ServiceEnum(str, Enum):
    gemini = "gemini"
    # gpt4 = "gpt4"


class HeaderDescription(BaseModel):
    header: str
    description: str

class TranscriptAnalysisRequest(BaseModel):
    headers: List[HeaderDescription]
    transcript: List[Dict[str, str]]