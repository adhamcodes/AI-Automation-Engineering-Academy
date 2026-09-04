class Agent:
    def act(self, action: str, approved: bool = False) -> str:
        # Deliberate defect: approval is ignored.
        if action == "lookup":
            return "looked_up"
        if action == "send_report":
            return "sent"
        if action == "delete_data":
            return "deleted"
        return "unknown"
