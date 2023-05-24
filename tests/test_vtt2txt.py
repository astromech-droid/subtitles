import filecmp
import glob

from subtitles import vtt2txt
from subtitles.conf import settings

TEST_LINES: list[tuple[str]] = [
    ("00:00:09.083", "(THEME MUSIC PLAYING)"),
    ("00:00:31.750", "BONNIE: <i>We're real proud of you, Judy.</i>"),
    ("00:00:33.333", "STU: Yeah, scared too. BONNIE: Yes."),
]


def test_read():
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/vtt2txt/read.vtt")[0]

    assert vtt2txt.read(path) == TEST_LINES


def test_save(tmp_path):
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/vtt2txt/save.txt")[0]
    _path: str = tmp_path / "test.txt"

    vtt2txt.save(_path, TEST_LINES)

    assert filecmp.cmp(path, _path)
