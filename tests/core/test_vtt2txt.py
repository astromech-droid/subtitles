import settings as s
from utils import files

from core import vtt2txt


def test_parse_lines():
    input_path = files.find_path(s.TEST_DATA_DIR, "parse_lines_before.vtt")
    output_path = files.find_path(s.TEST_DATA_DIR, "parse_lines_after.txt")

    input = files.get_lines(input_path)
    output = files.get_lines(output_path)

    assert vtt2txt.parse_lines(input) == output


def test_parse_subtitles(tmp_path):
    from_path: str = files.find_path(s.TEST_DATA_DIR, "parse_subtitles_before.vtt")
    to_path = tmp_path / "tmp.txt"

    vtt2txt.parse_subtitles(from_path, to_path)

    expected_path: str = files.find_path(s.TEST_DATA_DIR, "parse_subtitles_after.txt")
    expected: list = files.get_lines(expected_path)

    assert files.get_lines(to_path) == expected
