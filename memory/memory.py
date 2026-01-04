class Memory:
    def __init__(self):
        self.history = []

    def add(self, query: str, response: str):
        self.history.append({
            "query": query,
            "response": response
        })

    def get_last(self):
        if not self.history:
            return None
        return self.history[-1]

    def get_all(self):
        return self.history
