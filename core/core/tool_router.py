from tools.calculator import calculate


def route_tool(intent: str, query: str) -> str:
    """
    Routes the query to the correct tool based on intent.
    """
    if intent == "math":
        return calculate(query)

    return None
