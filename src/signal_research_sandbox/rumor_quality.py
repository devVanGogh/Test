"""Simple source/rumor flags for permitted, timestamped, untrusted events."""
import hashlib
import re
from datetime import datetime, timezone

FLAGS = ("guaranteed profit", "act now", "exclusive insider", "zero risk", "secret tip")

def normalize_content(content):
    if not isinstance(content, str):
        raise TypeError("content must be str")
    return re.sub(r"\s+", " ", content.strip().casefold())

def event_fingerprint(content):
    return hashlib.sha256(normalize_content(content).encode("utf-8")).hexdigest()

def _utc(timestamp):
    dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timezone required")
    return dt.astimezone(timezone.utc)

def inspect_event(event, decision_at):
    """Never infer trading odds from rumor. Disallow future/unpermitted content."""
    if event.get("access_granted") is not True:
        raise PermissionError("no source access permission")
    if event.get("source_class") not in ("licensed_news", "permitted_public", "synthetic"):
        raise PermissionError("disallowed source class")
    if _utc(event["available_at"]) > _utc(decision_at):
        raise ValueError("future-event leakage")
    text = normalize_content(event["content"])
    return {
        "event_id": event["event_id"],
        "fingerprint": event_fingerprint(event["content"]),
        "risk_flags": [flag for flag in FLAGS if flag in text],
        "verified": False,
        "predicted_probability": None,
    }
