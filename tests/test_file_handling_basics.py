from src.file_handling_basics import (
    find_lines_containing,
    read_text_file,
    summarize_log_file,
    write_text_file,
)


def test_write_and_read_text_file(tmp_path):
    path = tmp_path / "sample.log"
    write_text_file(str(path), "INFO ok")
    assert read_text_file(str(path)) == "INFO ok"


def test_find_lines_containing(tmp_path):
    path = tmp_path / "sample.log"
    write_text_file(str(path), "INFO ok\nERROR failed\n")
    assert find_lines_containing(str(path), "error") == ["ERROR failed"]


def test_summarize_log_file(tmp_path):
    path = tmp_path / "sample.log"
    write_text_file(str(path), "INFO ok\nWARNING retry\nERROR failed\n")
    assert summarize_log_file(str(path)) == {"INFO": 1, "WARNING": 1, "ERROR": 1}
