# agents.py

from response_generator import ResponseGenerator

class CodeAgent:
    def __init__(self):
        self.generator = ResponseGenerator()
        self.system_prompt = """
        You are an AI code generation assistant specialized in building software projects.

        Guidelines:
        - If the user asks for a full project, structure it clearly (e.g. folders, files).
        - If the user specifies a stack (language, framework, tools) in their prompt, follow it exactly.
        - If no stack is specified, suggest 2-5 relevant basic to advance tech based on implementation difficulty levels stacks and ask the user to choose before proceeding.
        - Once confirmed, build out the project step by step — include core files and essential setup.
        - Always write clean, production-ready code.
        - Include comments only for complex logic.
        - Do not include explanations unless the user explicitly asks.
        - Use appropriate file/folder names and clearly separate backend, frontend, and config files when relevant.
        """

    def generate_code(self, instruction: str, language: str = "auto") -> str:
        prompt_parts = [self.system_prompt.strip()]

        if language.lower() != "auto":
            prompt_parts.append(f"Target language: {language}")

        prompt_parts.append(f"Instruction: {instruction.strip()}")
        prompt = "\n\n".join(prompt_parts)

        return self.generator.call_groq(prompt)

    def review_code(self, code: str) -> str:
        prompt = f"{self.system_prompt}\n\nReview this code and suggest improvements:\n\n{code}"
        return self.generator.call_groq(prompt)

    def explain_code(self, code: str) -> str:
        prompt = f"{self.system_prompt}\n\nExplain this code step by step:\n\n{code}"
        return self.generator.call_groq(prompt)


