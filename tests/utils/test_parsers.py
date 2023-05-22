import os

import settings as s

from utils import parsers


def test_remove_linenumbers():
    test_input_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/remove_linenumbers_before.vtt"
    )
    test_output_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/remove_linenumbers_after.vtt"
    )

    with open(test_input_file, "r", encoding="utf-8-sig") as f_input:
        test_input = f_input.readlines()

    with open(test_output_file, "r", encoding="utf-8-sig") as f_output:
        test_output = f_output.readlines()

    assert parsers.remove_linenumbers(test_input) == test_output


def test_remove_headers():
    test_input_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/remove_headers_before.vtt"
    )
    test_output_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/remove_headers_after.vtt"
    )

    with open(test_input_file, "r", encoding="utf-8-sig") as f_input:
        test_input = f_input.readlines()

    with open(test_output_file, "r", encoding="utf-8-sig") as f_output:
        test_output = f_output.readlines()

    assert parsers.remove_headers(test_input) == test_output


def test_remove_blanklines():
    test_input_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/remove_blanklines_before.vtt"
    )
    test_output_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/remove_blanklines_after.vtt"
    )

    with open(test_input_file, "r") as f_input:
        test_input = f_input.readlines()

    with open(test_output_file, "r") as f_output:
        test_output = f_output.readlines()

    assert parsers.remove_blanklines(test_input) == test_output


def test_extruct_starttime():
    test_input_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/extruct_starttime_before.vtt"
    )
    test_output_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/extruct_starttime_after.vtt"
    )

    with open(test_input_file, "r") as f_input:
        test_input = f_input.readlines()

    with open(test_output_file, "r") as f_output:
        test_output = f_output.readlines()

    assert parsers.extruct_starttime(test_input) == test_output


def test_put_starttime_on_alllines():
    test_input_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/put_starttime_on_alllines_before.txt"
    )
    test_output_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/put_starttime_on_alllines_after.txt"
    )

    with open(test_input_file, "r") as f_input:
        test_input = f_input.readlines()

    with open(test_output_file, "r") as f_output:
        test_output = f_output.readlines()

    assert parsers.put_starttime_on_alllines(test_input) == test_output


def test_merge_multilines():
    test_input_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/merge_multilines_before.txt"
    )
    test_output_file = os.path.join(
        s.TEST_DATA_DIR, "utils/parsers/merge_multilines_after.txt"
    )

    with open(test_input_file, "r") as f_input:
        test_input = f_input.readlines()

    with open(test_output_file, "r") as f_output:
        test_output = f_output.readlines()

    assert parsers.merge_multilines(test_input) == test_output
