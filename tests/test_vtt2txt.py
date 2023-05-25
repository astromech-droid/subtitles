import filecmp
import glob

from subtitles import vtt2txt
from subtitles.conf import settings


def test_read():
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/vtt2txt/read.vtt")[0]

    assert vtt2txt.read(path) == settings.TEST_LINES_VTT


def test_save(tmp_path):
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/vtt2txt/save.txt")[0]
    _path: str = tmp_path / "test.txt"

    vtt2txt.save(_path, settings.TEST_LINES_VTT)

    assert filecmp.cmp(path, _path)
