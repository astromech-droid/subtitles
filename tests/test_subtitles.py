import filecmp
import glob
import os

import pytest
from subtitles.conf import settings
from subtitles.subtitles import Subtitles


@pytest.fixture
def clean_up():
    yield

    dirnames: list[str] = [
        os.path.join(settings.VTT_DIR, settings.TEST_TITLE),
        os.path.join(settings.XML_DIR, settings.TEST_TITLE),
    ]

    for dirname in dirnames:
        if os.path.exists(dirname):
            for _path in glob.glob(f"{dirname}/*"):
                os.remove(_path)

            os.removedirs(dirname)


def test_download_vtt(clean_up):
    service: str = settings.SERVICE_DISNEYPLUS
    title: str = settings.TEST_TITLE
    subtitles = Subtitles(service, title)

    url: str = settings.TEST_URL_DISNEYPLUS_00

    pathes: list[str] = subtitles.download(url)
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/downloader/seg_00000.vtt")[0]

    assert filecmp.cmp(path, pathes[0])


def test_download_xml(clean_up):
    service: str = settings.SERVICE_NETFLIX
    title: str = settings.TEST_TITLE
    subtitles = Subtitles(service, title)

    url: str = settings.TEST_URL_NETFLIX

    pathes: list[str] = subtitles.download(url)
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/downloader/subtitles.xml")[0]

    assert filecmp.cmp(path, pathes[0])


def test_read_vtt():
    service: str = settings.SERVICE_DISNEYPLUS
    title: str = settings.TEST_TITLE
    subtitles = Subtitles(service, title)

    path: str = glob.glob(f"{settings.TEST_DATA_DIR}*/vtt2txt/read.vtt")[0]

    assert subtitles.read(path) == settings.TEST_LINES_VTT


def test_read_xml():
    service: str = settings.SERVICE_NETFLIX
    title: str = settings.TEST_TITLE
    subtitles = Subtitles(service, title)

    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/xml2txt/read.xml")[0]

    assert subtitles.read(path) == settings.TEST_LINES_XML


def test_write_vtt(tmp_path):
    service: str = settings.SERVICE_DISNEYPLUS
    title: str = settings.TEST_TITLE
    subtitles = Subtitles(service, title)

    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/vtt2txt/write.txt")[0]
    _path: str = tmp_path / "test.txt"

    subtitles.write(_path, settings.TEST_LINES_VTT)

    assert filecmp.cmp(path, _path)


def test_write_xml(tmp_path):
    service: str = settings.SERVICE_NETFLIX
    title: str = settings.TEST_TITLE
    subtitles = Subtitles(service, title)

    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/xml2txt/write.txt")[0]
    _path: str = tmp_path / "test.txt"

    subtitles.write(_path, settings.TEST_LINES_XML)

    assert filecmp.cmp(path, _path)
