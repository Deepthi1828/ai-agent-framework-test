from core.agent import Agent


def main():
    print("AI Agent Framework")
    print("------------------")

    agent = Agent()
    user_input = input("Enter your task: ")

    result = agent.run(user_input)

    print("\nAgent Output:")
    print(result)


if __name__ == "__main__":
    main()
