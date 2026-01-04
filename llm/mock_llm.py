from llm.llm_interface import LLMInterface

class MockLLM(LLMInterface):
    def generate(self, prompt: str) -> str:
        return f"[MockLLM Response] {prompt}"