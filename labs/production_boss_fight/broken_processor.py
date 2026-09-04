from __future__ import annotations


class Processor:
    """Deliberately broken production state processor.

    The constructor accepts a state path because the production contract requires
    durable state, but this implementation ignores it on purpose.
    """

    def __init__(self, state_path: str) -> None:
        self.state_path = state_path
        self.total = 0

    def process(self, event_id: str, amount: int) -> dict[str, int | str]:
        # Deliberate defects:
        # - no durable persistence across a new Processor instance
        # - no idempotency for duplicate event IDs
        # - no input validation
        self.total += amount
        return {"status": "processed", "total": self.total}
