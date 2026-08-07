from src.fundamentals import classify_password_length, count_failed_logins, normalize_username


def test_classify_password_length():
    assert classify_password_length("short") == "weak"
    assert classify_password_length("medium99") == "medium"
    assert classify_password_length("verylongpassword") == "strong"


def test_count_failed_logins():
    logs = ["ok", "failed login", "FAILED LOGIN"]
    assert count_failed_logins(logs) == 2


def test_normalize_username():
    assert normalize_username(" Alice ") == "alice"
