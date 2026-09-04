class Processor:
    def __init__(self) -> None:
        self.total = 0
        self.processed_ids: set[str] = set()

    def process(self, event_id: str, amount: int) -> dict:
        # Deliberate defect: duplicates still change business state.
        self.total += amount
        self.processed_ids.add(event_id)
        return {"status": "processed", "total": self.total}
