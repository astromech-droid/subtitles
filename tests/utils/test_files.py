import settings

from utils import files


def test_find_found():
    root_dir = settings.TEST_DATA_DIR
    filename = "find.txt"  # This file exists.
    excepted_text = "tests/data/utils/files/find.txt"
    assert files.find(root_dir, filename) == excepted_text


def test_find_notfound():
    root_dir = settings.TEST_DATA_DIR
    filename = "notfound.txt"  # This file doesn't exist.
    excepted_text = ""
    assert files.find(root_dir, filename) == excepted_text


def test_get_lines():
    root_dir = settings.TEST_DATA_DIR
    filename = "get_lines.txt"
    path = files.find(root_dir, filename)
    excepted: list = ["Hello world!\n", "This is a test."]

    assert files.get_lines(path) == excepted
