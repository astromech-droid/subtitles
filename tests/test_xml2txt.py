import filecmp
import glob

from subtitles import xml2txt
from subtitles.conf import settings

TEST_LINES: list[tuple[str]] = [
    ("00:13:25.000", "-Leave town for adventure. -[both] What did you say?"),
    ("00:10:21.454", "But we've been here for all time, since I was born!"),
    ("00:01:45.063", "You can handle a few minutes up here."),
]


def test_read():
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/*/read.xml")[0]

    assert xml2txt.read(path) == TEST_LINES


def test_save(tmp_path):
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/*/save.txt")[0]
    _path: str = tmp_path / "test.txt"

    xml2txt.save(_path, TEST_LINES)

    assert filecmp.cmp(path, _path)
