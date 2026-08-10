"""Practice lists and dictionaries with security-style data."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.collections_practice import (
    build_user_record,
    count_events_by_type,
    filter_high_risk_events,
    unique_usernames,
)


raw_usernames = [" Alice ", "bob", "ALICE", "charlie", "bob"]
print("Unique usernames:", unique_usernames(raw_usernames))

events = [
    {"type": "login", "risk_score": 20},
    {"type": "failed_login", "risk_score": 75},
    {"type": "failed_login", "risk_score": 90},
    {"type": "file_change", "risk_score": 60},
]

print("Event counts:", count_events_by_type(events))
print("High-risk events:", filter_high_risk_events(events))
print("User record:", build_user_record(" Dana ", " Analyst "))
