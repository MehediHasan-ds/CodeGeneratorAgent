# endpoints.py

from fastapi import APIRouter, HTTPException
from response_generator import PromptRequest
from agents import CodeAgent

router = APIRouter()
agent = CodeAgent()

@router.post("/generate")
async def generate_response(request: PromptRequest):
    try:
        response = agent.generate_code(
            instruction=request.prompt,
            language=request.language
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

