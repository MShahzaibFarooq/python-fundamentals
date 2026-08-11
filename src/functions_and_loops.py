"""Practice functions and loops with beginner security-style examples."""


def count_matching_lines(lines: list[str], keyword: str) -> int:
    """Count how many lines contain a keyword, case-insensitively."""
    keyword = keyword.lower()
    count = 0
    for line in lines:
        if keyword in line.lower():
            count += 1
    return count


def collect_failed_users(log_lines: list[str]) -> list[str]:
    """Extract usernames from simple failed-login log lines.

    Expected line format:
    "failed login: username"
    """
    users = []
    for line in log_lines:
        if line.lower().startswith("failed login:"):
            username = line.split(":", 1)[1].strip().lower()
            if username:
                users.append(username)
    return users


def calculate_average(numbers: list[float]) -> float:
    """Calculate an average using a loop."""
    if not numbers:
        return 0.0

    total = 0.0
    for number in numbers:
        total += number
    return total / len(numbers)


def create_numbered_findings(findings: list[str]) -> list[str]:
    """Return findings with readable numbers."""
    numbered = []
    for index, finding in enumerate(findings, start=1):
        numbered.append(f"{index}. {finding}")
    return numbered
