import filecmp
import glob

from cli.merger import Merger
from subtitles import settings


def test_merge(tmp_path):
    dirname_src: str = f"{settings.TEST_DATA_DIR}/merger"
    dirname_dst: str = tmp_path / settings.DEFAULT_TXT_FILENAME

    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/merger/subtitles.txt")[0]
    _path = Merger().merge(dirname_src, dirname_dst)

    assert filecmp.cmp(path, _path)
