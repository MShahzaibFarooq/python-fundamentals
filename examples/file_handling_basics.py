"""Practice reading, writing, and searching a small log file."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.file_handling_basics import (
    find_lines_containing,
    read_text_file,
    summarize_log_file,
    write_text_file,
)


log_path = "sample_output/week1_demo.log"
content = """INFO login successful
WARNING password retry
ERROR failed login
INFO logout
"""

write_text_file(log_path, content)

print("File content:")
print(read_text_file(log_path).strip())
print("Error lines:", find_lines_containing(log_path, "error"))
print("Summary:", summarize_log_file(log_path))
