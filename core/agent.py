from core.task_analyzer import analyze_task
from core.planner import create_plan
from core.reasoning import generate_reasoning
from memory.memory import Memory
from tools.calculator import calculate


class Agent:
    """
    Central controller of the AI Agent Framework.
    Handles task analysis, planning, reasoning, tool execution, and memory.
    """

    def __init__(self):
        self.memory = Memory()

    def run(self, user_input: str) -> str:
        # Store user input in memory
        self.memory.add(f"User Input: {user_input}")

        # Analyze task type
        analysis = analyze_task(user_input)
        task_type = analysis["task_type"]

        # -------------------------------------------------
        # TOOL EXECUTION (Task 1)
        # -------------------------------------------------
        if task_type == "tool":
            lower_input = user_input.lower()

            # Extract expression safely after 'calculate'
            expression = lower_input.split("calculate", 1)[1].strip()

            result = calculate(expression)
            self.memory.add(f"Tool Result: {result}")

            return (
                "AI Agent Execution\n"
                "------------------\n"
                "Task Type : tool\n"
                f"Calculation Result : {result}"
            )

        # -------------------------------------------------
        # PLANNING & GENERAL TASKS (Task 2 & Task 3)
        # -------------------------------------------------
        plan = create_plan(task_type, user_input)
        reasoning = generate_reasoning(plan)

        response = (
            "AI Agent Execution\n"
            "------------------\n"
            f"Task Type : {task_type}\n\n"
            "Execution Plan & Reasoning:\n"
        )

        for index, (step, reason) in enumerate(zip(plan, reasoning), start=1):
            response += (
                f"{index}. {step}\n"
                f"   Reason: {reason}\n"
            )

        # Store completion in memory
        self.memory.add("Agent Response Generated")

        return response
