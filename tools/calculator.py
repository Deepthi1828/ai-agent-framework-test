def calculate(expression: str) -> str:
    """
    Executes a simple mathematical calculation safely.
    """

    try:
        # Normalize expression
        expression = expression.strip()

        # Replace common unicode multiplication symbols if any
        expression = expression.replace("×", "*").replace("÷", "/")

        if not expression:
            return "Invalid calculation"

        # Safe eval: disable builtins
        result = eval(expression, {"__builtins__": None}, {})

        return str(result)

    except Exception as e:
        return "Invalid calculation"
