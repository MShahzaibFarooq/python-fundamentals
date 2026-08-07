from src.fundamentals import classify_password_length, count_failed_logins


passwords = ["cat", "correcthorsebattery", "medium99"]
for password in passwords:
    print(password, "=>", classify_password_length(password))

logs = ["INFO login ok", "WARN failed login for alice", "WARN failed login for bob"]
print("Failed logins:", count_failed_logins(logs))
