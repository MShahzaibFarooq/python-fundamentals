"""Practice functions and loops with simple cybersecurity data."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.functions_and_loops import (
    calculate_average,
    collect_failed_users,
    count_matching_lines,
    create_numbered_findings,
)


logs = [
    "INFO: login successful: alice",
    "failed login: bob",
    "failed login: charlie",
    "WARNING: password retry",
    "failed login: bob",
]

print("Failed login count:", count_matching_lines(logs, "failed login"))
print("Failed users:", collect_failed_users(logs))
print("Average risk score:", calculate_average([30, 70, 90]))

findings = ["Weak password policy", "Multiple failed logins", "Missing audit notes"]
print("Numbered findings:")
for finding in create_numbered_findings(findings):
    print(finding)
