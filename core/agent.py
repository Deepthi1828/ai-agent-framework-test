from core.task_analyzer import analyze_task


class Agent:
    """
    Central controller of the AI Agent Framework.

    The Agent is responsible for:
    - Receiving user input
    - Analyzing the task type
    - Coordinating the execution flow
    - Returning a structured response
    """

    def run(self, user_input: str) -> str:
        """
        Executes the agent workflow for the given user input.

        Parameters:
            user_input (str): Input provided by the user.

        Returns:
            str: Structured response from the agent.
        """

        # Step 1: Analyze the task
        analysis = analyze_task(user_input)

        # Step 2: Prepare a structured response
        response = (
            "AI Agent Execution\n"
            "------------------\n"
            f"Task Type   : {analysis['task_type']}\n"
            f"User Input : {analysis['query']}\n"
        )

        return response
