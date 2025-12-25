def calculate(expression: str) -> str:
    """
    Executes a simple mathematical calculation.

    Parameters:
        expression (str): Mathematical expression as a string.

    Returns:
        str: Result of the calculation or error message.
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid calculation"
