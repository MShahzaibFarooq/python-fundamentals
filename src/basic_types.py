"""Helpers for practicing Python variables and basic data types."""


def describe_value(value: object) -> dict[str, str]:
    """Return a simple description of a Python value."""
    return {
        "type": type(value).__name__,
        "text": str(value),
    }


def is_truthy(value: object) -> bool:
    """Return Python's boolean interpretation of a value."""
    return bool(value)


def safe_int(value: str, default: int = 0) -> int:
    """Convert text to an integer, returning a default if conversion fails."""
    try:
        return int(value)
    except ValueError:
        return default


def login_risk_score(failed_logins: int, is_admin: bool) -> int:
    """Calculate a tiny practice risk score from beginner data types."""
    score = failed_logins * 10
    if is_admin:
        score += 20
    return score
