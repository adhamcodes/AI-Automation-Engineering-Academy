CREATE TABLE automation_events (
    event_id TEXT PRIMARY KEY,
    status TEXT NOT NULL CHECK (status IN ('received','processing','completed','failed')),
    attempt_count INTEGER NOT NULL DEFAULT 0 CHECK (attempt_count >= 0),
    last_error TEXT,
    result_ref TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
