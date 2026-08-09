"""Practice variables, data types, casting, and simple security logic."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.basic_types import describe_value, is_truthy, login_risk_score, safe_int


username = "alice"
failed_login_text = "3"
is_admin = True

failed_logins = safe_int(failed_login_text)
risk_score = login_risk_score(failed_logins, is_admin)

print("Username:", username)
print("Failed logins:", failed_logins)
print("Is admin:", is_admin)
print("Risk score:", risk_score)
print("Username description:", describe_value(username))
print("Failed login text is truthy:", is_truthy(failed_login_text))
