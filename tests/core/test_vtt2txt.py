import filecmp
import glob

from cli.conf import settings
from cli.core.vtt2txt import Vtt2txt


def test_read():
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/vtt2txt/read.vtt")[0]

    assert Vtt2txt().read(path) == settings.TEST_LINES_VTT


def test_write(tmp_path):
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/vtt2txt/write.txt")[0]
    _path: str = tmp_path / "test.txt"

    Vtt2txt().write(_path, settings.TEST_LINES_VTT)

    assert filecmp.cmp(path, _path)
