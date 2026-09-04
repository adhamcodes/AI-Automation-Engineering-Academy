from __future__ import annotations


def normalize_customer(payload: dict) -> dict:
    name = str(payload.get("name", "")).strip()
    email = str(payload.get("email", "")).strip().lower()
    if not name:
        raise ValueError("name is required")
    if "@" not in email:
        raise ValueError("valid email is required")
    return {"name": name, "email": email, "source": payload.get("source", "unknown")}
