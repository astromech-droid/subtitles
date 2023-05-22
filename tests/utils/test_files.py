import settings

from utils import files


def test_find_path_found():
    root_dir = settings.TEST_DATA_DIR
    filename = "find_path.txt"  # This file exists.
    excepted_text = "tests/data/utils/files/find_path.txt"
    assert files.find_path(root_dir, filename) == excepted_text


def test_find_path_notfound():
    root_dir = settings.TEST_DATA_DIR
    filename = "notfound.txt"  # This file doesn't exist.
    excepted_text = ""
    assert files.find_path(root_dir, filename) == excepted_text


def test_get_lines():
    root_dir = settings.TEST_DATA_DIR
    filename = "get_lines.txt"
    path = files.find_path(root_dir, filename)
    excepted: list = ["Hello world!\n", "This is a test."]

    assert files.get_lines(path) == excepted
