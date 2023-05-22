import settings as s

from utils import files, parsers


def test_remove_linenumbers():
    input_path: str = files.find_path(s.TEST_DATA_DIR, "remove_linenumbers_before.vtt")
    output_path: str = files.find_path(s.TEST_DATA_DIR, "remove_linenumbers_after.vtt")

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.remove_linenumbers(input) == output


def test_remove_headers():
    input_path: str = files.find_path(s.TEST_DATA_DIR, "remove_headers_before.vtt")
    output_path: str = files.find_path(s.TEST_DATA_DIR, "remove_headers_after.vtt")

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.remove_headers(input) == output


def test_remove_blanklines():
    input_path: str = files.find_path(s.TEST_DATA_DIR, "remove_blanklines_before.vtt")
    output_path: str = files.find_path(s.TEST_DATA_DIR, "remove_blanklines_after.vtt")

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.remove_blanklines(input) == output


def test_extruct_starttime():
    input_path: str = files.find_path(s.TEST_DATA_DIR, "extruct_starttime_before.vtt")
    output_path: str = files.find_path(s.TEST_DATA_DIR, "extruct_starttime_after.vtt")

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.extruct_starttime(input) == output


def test_put_starttime_on_alllines():
    input_path: str = files.find_path(
        s.TEST_DATA_DIR, "put_starttime_on_alllines_before.txt"
    )
    output_path: str = files.find_path(
        s.TEST_DATA_DIR, "put_starttime_on_alllines_after.txt"
    )

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.put_starttime_on_alllines(input) == output


def test_merge_multilines():
    input_path: str = files.find_path(s.TEST_DATA_DIR, "merge_multilines_before.txt")
    output_path: str = files.find_path(s.TEST_DATA_DIR, "merge_multilines_after.txt")

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.merge_multilines(input) == output
