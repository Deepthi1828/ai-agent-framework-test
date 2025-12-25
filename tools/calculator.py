print(">>> CALCULATOR.PY IS EXECUTING <<<")
def calculate(expression: str) -> str:
    try:
        expression = expression.strip()
        if not expression:
            return "Invalid calculation"

        return str(eval(expression))
    except Exception:
        return "Invalid calculation"
