import math
import re


def calculate(expression: str) -> str:
    """
    Safely evaluates mathematical expressions.
    Supports basic arithmetic and common math functions.
    """

    try:
        # Remove non-math words
        cleaned = re.sub(
            r"[a-zA-Z]", "", expression
        )

        # Allowed math functions
        allowed_names = {
            "sqrt": math.sqrt,
            "pow": math.pow,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "pi": math.pi,
            "e": math.e
        }

        result = eval(cleaned, {"__builtins__": {}}, allowed_names)
        return f"Calculation Result: {result}"

    except Exception:
        return "Unable to calculate the given expression"
