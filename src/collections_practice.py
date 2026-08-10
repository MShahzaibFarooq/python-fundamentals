"""Beginner helpers for practicing lists and dictionaries."""


def unique_usernames(usernames: list[str]) -> list[str]:
    """Return usernames once, preserving first-seen order."""
    seen = set()
    result = []
    for username in usernames:
        normalized = username.strip().lower()
        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(normalized)
    return result


def count_events_by_type(events: list[dict[str, str]]) -> dict[str, int]:
    """Count security-style events by their type field."""
    counts: dict[str, int] = {}
    for event in events:
        event_type = event.get("type", "unknown")
        counts[event_type] = counts.get(event_type, 0) + 1
    return counts


def filter_high_risk_events(events: list[dict[str, object]], minimum_score: int = 70) -> list[dict[str, object]]:
    """Return events whose risk score is greater than or equal to the threshold."""
    return [event for event in events if int(event.get("risk_score", 0)) >= minimum_score]


def build_user_record(username: str, role: str, active: bool = True) -> dict[str, object]:
    """Create a small user record dictionary."""
    return {
        "username": username.strip().lower(),
        "role": role.strip().lower(),
        "active": active,
    }
