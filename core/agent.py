from core.task_analyzer import analyze_task
from core.planner import create_plan
from core.reasoning import generate_reasoning
from memory.memory import Memory
import re


class Agent:
    """
    Central controller of the AI Agent Framework.
    """

    def __init__(self):
        self.memory = Memory()

    # -------- LOCAL TOOL IMPLEMENTATION (NO IMPORT ISSUES) --------
    def _calculate(self, expression: str) -> str:
        try:
            expression = expression.strip()
            if not expression:
                return "Invalid calculation"
            return str(eval(expression))
        except Exception:
            return "Invalid calculation"

    def run(self, user_input: str) -> str:
        self.memory.add(f"User Input: {user_input}")

        analysis = analyze_task(user_input)
        task_type = analysis["task_type"]

        # ---------------- TOOL TASK ----------------
        if task_type == "tool":
            match = re.search(r'calculate\s+(.*)', user_input, re.IGNORECASE)

            if match:
                expression = match.group(1)
                result = self._calculate(expression)
            else:
                result = "Invalid calculation"

            self.memory.add(f"Tool Result: {result}")

            return (
                "AI Agent Execution\n"
                "------------------\n"
                "Task Type : tool\n"
                f"Calculation Result : {result}"
            )

        # ---------------- PLANNING & GENERAL ----------------
        plan = create_plan(task_type, user_input)
        reasoning = generate_reasoning(plan)

        response = (
            "AI Agent Execution\n"
            "------------------\n"
            f"Task Type : {task_type}\n\n"
            "Execution Plan & Reasoning:\n"
        )

        for i, (step, reason) in enumerate(zip(plan, reasoning), start=1):
            response += (
                f"{i}. {step}\n"
                f"   Reason: {reason}\n"
            )

        self.memory.add("Agent Response Generated")
        return response
