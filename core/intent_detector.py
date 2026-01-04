import re


def detect_intent(query: str) -> str:
    """
    Detects the intent of the user query.
    Returns:
    - "math" for calculation-related queries
    - "general" for all other queries
    """

    if not query:
        return "general"

    query_lower = query.lower().strip()

    # 1️⃣ Keyword-based math detection
    math_keywords = [
        "add", "addition", "sum", "plus",
        "subtract", "minus", "difference",
        "multiply", "multiplication", "product",
        "divide", "division", "quotient",
        "square", "cube", "power",
        "percentage", "percent",
        "average", "mean",
        "calculate", "solve", "evaluate"
    ]

    for word in math_keywords:
        if word in query_lower:
            return "math"

    # 2️⃣ Symbol-based detection
    math_symbols = ["+", "-", "*", "/", "%", "^"]
    for symbol in math_symbols:
        if symbol in query:
            return "math"

    # 3️⃣ Regex-based numeric expression detection
    pattern = r"\d+(\.\d+)?\s*[\+\-\*/%]\s*\d+(\.\d+)?"
    if re.search(pattern, query):
        return "math"

    # 4️⃣ Pure number input
    if query_lower.replace(".", "", 1).isdigit():
        return "math"

    return "general"
