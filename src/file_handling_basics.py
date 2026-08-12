"""Beginner file-handling helpers for cybersecurity practice."""

from pathlib import Path


def write_text_file(path: str, content: str) -> Path:
    """Write text to a file and return the Path object."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return file_path


def read_text_file(path: str) -> str:
    """Read a UTF-8 text file."""
    return Path(path).read_text(encoding="utf-8")


def find_lines_containing(path: str, keyword: str) -> list[str]:
    """Return lines that contain a keyword, case-insensitively."""
    keyword = keyword.lower()
    lines = read_text_file(path).splitlines()
    return [line for line in lines if keyword in line.lower()]


def summarize_log_file(path: str) -> dict[str, int]:
    """Count common beginner log levels in a text file."""
    levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in read_text_file(path).splitlines():
        for level in levels:
            if line.upper().startswith(level):
                levels[level] += 1
    return levels
