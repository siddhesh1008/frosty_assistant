class DecisionModel:
    """
    Classifies user queries into categories (general, realtime, automation)
    and routes them to the correct handler.
    """

    def __init__(self):
        # Placeholder: Load any model or rules needed for classification
        pass

    def classify(self, query: str) -> str:
        """
        Determines the type of query.
        Returns one of: "general", "realtime", "automation"
        """
        # Placeholder implementation (to be replaced with AI or rules)
        if any(word in query.lower() for word in ["weather", "news", "now"]):
            return "realtime"
        elif any(word in query.lower() for word in ["remind", "turn on", "open", "set"]):
            return "automation"
        else:
            return "general"
