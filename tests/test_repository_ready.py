from pathlib import Path


def test_repository_has_readme():
    assert Path("README.md").exists()


def test_repository_has_src_folder():
    assert Path("src").exists()
