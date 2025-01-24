from typing import Dict
import json
from schema import TranscriptAnalysisRequest
from gemini_processor import GeminiProcessor

async def transcript_analyze(payload: TranscriptAnalysisRequest) -> Dict[str, str]:
    try:
        gemini_processor = GeminiProcessor()

        # Combine headers and descriptions for LLM prompt
        combined_headers = [
            f"{header.header}: {header.description}"
            for header in payload.headers
        ]
        combined_prompt = "\n".join(combined_headers)

        # Generate analysis
        llm_response = await gemini_processor.getAnalytics(
            transcript=payload.transcript,
            prompt=(
                "Analyze the transcript based on the following fields and descriptions analysis (limit to one line per header):\n" + combined_prompt
            )
        )
        final_analysis = {}

        for header in payload.headers:
            analytics = llm_response.get("analytics")
            if analytics and header.header in analytics:
                analysis = analytics[header.header]
            else:
                analysis = "Error generating analysis"
            final_analysis[header.header] = analysis

        return final_analysis

    except Exception as e:
        raise Exception(f"Error analyzing transcript: {str(e)}")
    

