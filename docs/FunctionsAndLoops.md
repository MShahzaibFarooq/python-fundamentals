# Functions and Loops

## Functions

A function is a reusable block of code. Functions help keep programs organized and easier to test.

```python
def normalize_username(username):
    return username.strip().lower()
```

## Loops

A loop repeats work over a collection of values.

```python
for line in log_lines:
    print(line)
```

## Why this matters in cybersecurity

Security scripts often process repeated data:

- log lines,
- usernames,
- IP addresses,
- file paths,
- findings,
- alerts.

Functions keep this logic reusable. Loops let the program process many records.

## Practice task

Create a function that loops through log lines and counts how many contain a chosen keyword.
