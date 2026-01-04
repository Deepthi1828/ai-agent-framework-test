"""
Main entry point for AI Agent Framework
"""

from llm.mock_llm import MockLLM


class AIAgent:
    def __init__(self, llm):
        self.llm = llm

    def handle_query(self, query: str) -> str:
        """
        Handles any user query using the LLM
        """
        return self.llm.generate(query)


def main():
    print("=== AI Agent Framework ===")
    print("Type 'exit' to quit\n")

    llm = MockLLM()
    agent = AIAgent(llm)

    while True:
        user_query = input("Enter your query: ")

        if user_query.lower() == "exit":
            print("Exiting AI Agent. Goodbye!")
            break

        response = agent.handle_query(user_query)
        print("Agent Response:", response)
        print("-" * 40)


if __name__ == "__main__":
    main()
