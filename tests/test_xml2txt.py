import filecmp
import glob

from subtitles import xml2txt
from subtitles.conf import settings


def test_read():
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/*/read.xml")[0]

    assert xml2txt.read(path) == settings.TEST_LINES_XML


def test_write(tmp_path):
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/*/save.txt")[0]
    _path: str = tmp_path / "test.txt"

    xml2txt.write(_path, settings.TEST_LINES_XML)

    assert filecmp.cmp(path, _path)
