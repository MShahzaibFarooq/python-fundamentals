from src.fundamentals import normalize_username


raw_names = [" Alice ", "BOB", "  charlie"]
normalized = [normalize_username(name) for name in raw_names]

print("Normalized usernames:")
for name in normalized:
    print("-", name)
