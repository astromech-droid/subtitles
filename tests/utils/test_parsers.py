from subtitles.conf import settings
from subtitles.utils import files, parsers


def test_remove_linenumbers():
    input_path: str = files.find_path(
        settings.TEST_DATA_DIR, "remove_linenumbers_before.vtt"
    )
    output_path: str = files.find_path(
        settings.TEST_DATA_DIR, "remove_linenumbers_after.vtt"
    )

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.remove_linenumbers(input) == output


def test_remove_headers():
    input_path: str = files.find_path(settings.TEST_DATA_DIR, "remove_headers_before.vtt")
    output_path: str = files.find_path(settings.TEST_DATA_DIR, "remove_headers_after.vtt")

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.remove_headers(input) == output


def test_remove_blanklines():
    input_path: str = files.find_path(
        settings.TEST_DATA_DIR, "remove_blanklines_before.vtt"
    )
    output_path: str = files.find_path(
        settings.TEST_DATA_DIR, "remove_blanklines_after.vtt"
    )

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.remove_blanklines(input) == output


def test_extruct_starttime():
    input_path: str = files.find_path(
        settings.TEST_DATA_DIR, "extruct_starttime_before.vtt"
    )
    output_path: str = files.find_path(
        settings.TEST_DATA_DIR, "extruct_starttime_after.vtt"
    )

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.extruct_starttime(input) == output


def test_put_starttime_on_alllines():
    input_path: str = files.find_path(
        settings.TEST_DATA_DIR, "put_starttime_on_alllines_before.txt"
    )
    output_path: str = files.find_path(
        settings.TEST_DATA_DIR, "put_starttime_on_alllines_after.txt"
    )

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.put_starttime_on_alllines(input) == output


def test_merge_multilines():
    input_path: str = files.find_path(
        settings.TEST_DATA_DIR, "merge_multilines_before.txt"
    )
    output_path: str = files.find_path(
        settings.TEST_DATA_DIR, "merge_multilines_after.txt"
    )

    input: list = files.get_lines(input_path)
    output: list = files.get_lines(output_path)

    assert parsers.merge_multilines(input) == output


def test_extruct_elements():
    from bs4.element import NavigableString, Tag

    path = files.find_path(settings.TEST_DATA_DIR, "subtitles.xml")
    lines = files.get_lines(path)
    elements = parsers.extruct_elements(lines)

    for el in elements:
        if type(el) == NavigableString:
            pass
        elif type(el) == Tag:
            pass
        else:
            assert False


def test_to_int():
    starttime_str = "13817916667t"
    starttime_int = parsers._to_int(starttime_str)

    assert starttime_int == 13817916667


def _get_element():
    path = files.find_path(settings.TEST_DATA_DIR, "subtitles.xml")
    lines = files.get_lines(path)
    elements = parsers.extruct_elements(lines)

    return elements[0]


def test_get_seconds():
    element = _get_element()

    assert parsers._get_seconds(element) == 69166667 / 10000000


def test_to_time_str():
    seconds: float = 69166667 / 10000000

    assert parsers._to_time_str(seconds) == "00:00:06.917"


def test_get_starttime():
    element = _get_element()

    assert parsers.get_starttime(element) == "00:00:06.917"


def test_get_texts_recursively():
    element = _get_element()
    texts = ["'Cause it looks way cooler", "when I do this!"]

    assert parsers._get_texts_recursively(element) == texts


def test_get_text():
    element = _get_element()
    text = "'Cause it looks way cooler when I do this!"

    assert parsers.get_text(element) == text
