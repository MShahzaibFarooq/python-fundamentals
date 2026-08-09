from src.basic_types import describe_value, is_truthy, login_risk_score, safe_int


def test_describe_value():
    assert describe_value("alice") == {"type": "str", "text": "alice"}
    assert describe_value(10) == {"type": "int", "text": "10"}


def test_is_truthy():
    assert is_truthy("hello") is True
    assert is_truthy("") is False


def test_safe_int():
    assert safe_int("42") == 42
    assert safe_int("bad", default=-1) == -1


def test_login_risk_score():
    assert login_risk_score(3, False) == 30
    assert login_risk_score(3, True) == 50
