def classify_password_length(password: str) -> str:
    if len(password) < 8:
        return "weak"
    if len(password) < 12:
        return "medium"
    return "strong"


def count_failed_logins(lines: list[str]) -> int:
    return sum(1 for line in lines if "failed login" in line.lower())


def normalize_username(username: str) -> str:
    return username.strip().lower()
