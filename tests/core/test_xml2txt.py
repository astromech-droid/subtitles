from subtitles.conf import settings as s
from subtitles.core import xml2txt
from subtitles.utils import files


def test_parse_lines():
    input_path = files.find_path(s.TEST_DATA_DIR, "parse_lines_before_xml.xml")
    output_path = files.find_path(s.TEST_DATA_DIR, "parse_lines_after_xml.txt")

    input = files.get_lines(input_path)
    output = files.get_lines(output_path)

    assert xml2txt.parse_lines(input) == output


def test_parse_subtitles(tmp_path):
    from_path: str = files.find_path(s.TEST_DATA_DIR, "parse_subtitles_before_xml.xml")
    to_path = tmp_path / "tmp.txt"

    xml2txt.parse_subtitles(from_path, to_path)

    expected_path: str = files.find_path(s.TEST_DATA_DIR, "parse_subtitles_after_xml.txt")
    expected: list = files.get_lines(expected_path)

    assert files.get_lines(to_path) == expected
