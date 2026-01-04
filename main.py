from llm.mock_llm import MockLLM
from core.intent_detector import detect_intent
from core.agent import Agent
from memory.memory import Memory


class AIAgent:
    def __init__(self, llm):
        self.llm = llm
        self.memory = Memory()

    def handle_query(self, query: str) -> str:
        # Handle memory-based follow-up questions
        if "last" in query.lower():
            last = self.memory.get_last()
            if last:
                return f"Last Query: {last['query']} | Response: {last['response']}"
            return "No previous memory available."

        # Detect intent
        intent = detect_intent(query)

        # Route to appropriate tool
        tool_result = route_tool(intent, query)

        # Decide final response
        if tool_result:
            response = tool_result
        else:
            response = self.llm.generate(query)

        # Store in memory
        self.memory.add(query, response)
        return response


def main():
    print("=== Intelligent AI Agent Framework ===")
    print("Type 'exit' to quit\n")

    agent = AIAgent(MockLLM())

    while True:
        query = input("Enter your query: ")

        if query.lower() == "exit":
            print("\nSession Memory:")
            for item in agent.memory.get_all():
                print(f"- {item['query']} -> {item['response']}")
            break

        response = agent.handle_query(query)
        print("Agent Response:", response)
        print("-" * 40)


if __name__ == "__main__":
    main()
    main()
