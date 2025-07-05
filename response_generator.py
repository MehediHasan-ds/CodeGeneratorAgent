# rsponse_generator.py

from groq import Groq
from pydantic import BaseModel
from config import Config


class PromptRequest(BaseModel):
    prompt: str
    language: str = "auto" #optioal, default to "auto"



class ResponseGenerator:
    def __init__(self):
        self.config = Config()
        self.groq_client = Groq(api_key=self.config.GROQ_API_KEY)
    
    def call_groq(self, prompt: str) -> str:
        try:
            response = self.groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.config.MODEL_ID,
                max_tokens=self.config.MAX_TOKENS,
                temperature=self.config.TEMPERATURE,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"

