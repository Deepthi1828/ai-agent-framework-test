def calculate(expression: str) -> str:
    """
    Executes a simple mathematical calculation.

    Parameters:
        expression (str): Mathematical expression (e.g., "10 * 5")

    Returns:
        str: Result of the calculation or 'Invalid calculation'
    """
    try:
        expression = expression.strip()

        # If expression is empty, return error
        if not expression:
            return "Invalid calculation"

        result = eval(expression)
        return str(result)

    except Exception:
        return "Invalid calculation"
