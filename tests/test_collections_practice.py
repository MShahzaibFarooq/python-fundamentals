from src.collections_practice import (
    build_user_record,
    count_events_by_type,
    filter_high_risk_events,
    unique_usernames,
)


def test_unique_usernames_preserves_order():
    assert unique_usernames([" Alice ", "bob", "ALICE"]) == ["alice", "bob"]


def test_count_events_by_type():
    events = [{"type": "login"}, {"type": "failed_login"}, {"type": "login"}]
    assert count_events_by_type(events) == {"login": 2, "failed_login": 1}


def test_filter_high_risk_events():
    events = [{"risk_score": 10}, {"risk_score": 70}, {"risk_score": 99}]
    assert filter_high_risk_events(events) == [{"risk_score": 70}, {"risk_score": 99}]


def test_build_user_record():
    assert build_user_record(" Alice ", " Admin ") == {
        "username": "alice",
        "role": "admin",
        "active": True,
    }
