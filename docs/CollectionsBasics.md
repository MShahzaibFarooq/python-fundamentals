# Lists and Dictionaries

## Lists

A list stores multiple values in order.

```python
usernames = ["alice", "bob", "charlie"]
```

Lists are useful when order matters or when you need to process many items.

## Dictionaries

A dictionary stores key-value pairs.

```python
event = {
    "type": "failed_login",
    "user": "alice",
    "risk_score": 75,
}
```

Dictionaries are useful for structured records such as users, alerts, logs, and scan results.

## Cybersecurity connection

Security scripts often use:

- lists for log lines, usernames, IP addresses, and file paths,
- dictionaries for alerts, findings, assets, and reports.

## Practice task

Create a list of login events, count each event type, and filter high-risk events.
