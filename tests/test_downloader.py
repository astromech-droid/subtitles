import filecmp
import os
import re

from subtitles.conf import settings
from subtitles.Downloader import Downloader


def test_download(tmp_path):
    path: str = tmp_path / "test.txt"
    url: str = "https://raw.githubusercontent.com/astromech-droid/subtitles/main/LICENSE"
    service: str = settings.SERVICE_DISNEYPLUS
    Downloader(service).download(url, path)

    with open(path, "r") as f:
        downloaded: str = f.read()

    with open("./LICENSE", "r") as g:
        expected: str = g.read()

    assert downloaded == expected


def test_get_urls():
    url: str = "https://this/is/a/test/seg_00000.vtt"
    service: str = settings.SERVICE_DISNEYPLUS
    urls: list[str] = Downloader(service).get_urls(url)

    for _url in urls:
        if not re.match(r"^https://.*/seg_\d{5}\.vtt$", _url):
            assert False


def test_get_dirname():
    service: str = settings.SERVICE_DISNEYPLUS
    title: str = "test"
    expected: str = os.path.join(settings.VTT_DIR, title)

    assert Downloader(service).get_dirname(title) == expected


def test_download_all(tmp_path):
    urls: list[str] = [
        "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils/http/vtt/disneyplus/seg_00000.vtt",
        "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils/http/vtt/disneyplus/seg_00001.vtt",
    ]
    service: str = settings.SERVICE_DISNEYPLUS
    dirname: str = tmp_path._str
    Downloader(service).download_all(urls, dirname)

    if not filecmp.cmp(
        os.path.join(dirname, "seg_00000.vtt"),
        os.path.join(settings.TEST_DATA_DIR, "downloader/seg_00000.vtt"),
    ):
        assert False

    if not filecmp.cmp(
        os.path.join(dirname, "seg_00001.vtt"),
        os.path.join(settings.TEST_DATA_DIR, "downloader/seg_00001.vtt"),
    ):
        assert False
