from src.functions_and_loops import (
    calculate_average,
    collect_failed_users,
    count_matching_lines,
    create_numbered_findings,
)


def test_count_matching_lines():
    lines = ["ERROR failed", "ok", "error again"]
    assert count_matching_lines(lines, "error") == 2


def test_collect_failed_users():
    logs = ["failed login: Alice", "INFO ok", "failed login: bob"]
    assert collect_failed_users(logs) == ["alice", "bob"]


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([]) == 0.0


def test_create_numbered_findings():
    assert create_numbered_findings(["A", "B"]) == ["1. A", "2. B"]
