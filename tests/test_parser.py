import filecmp
import glob
import os

from cli.parser import Parser
from subtitles import settings

SERVICE_VTT: str = settings.SERVICE_DISNEYPLUS
TITLE_VTT: str = settings.TEST_TITLE
ParserVtt = Parser(SERVICE_VTT, TITLE_VTT)

SERVICE_XML: str = settings.SERVICE_NETFLIX
TITLE_XML: str = settings.TEST_TITLE
ParserXml = Parser(SERVICE_XML, TITLE_XML)


def test_dirname_src_vtt():
    assert ParserVtt.dirname_src == os.path.join(settings.VTT_DIR, TITLE_VTT)


def test_dirname_src_xml():
    assert ParserXml.dirname_src == os.path.join(settings.XML_DIR, TITLE_XML)


def test_dirname_dst_vtt():
    assert ParserVtt.dirname_dst == os.path.join(settings.TXT_DIR, TITLE_VTT)


def test_dirname_dst_xml():
    assert ParserXml.dirname_dst == os.path.join(settings.TXT_DIR, TITLE_XML)


def test_read_vtt():
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/vtt2txt/read.vtt")[0]

    assert ParserVtt.read(path) == settings.TEST_LINES_VTT


def test_read_xml():
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/xml2txt/read.xml")[0]

    assert ParserXml.read(path) == settings.TEST_LINES_XML


def test_write_xml(tmp_path):
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/xml2txt/write.txt")[0]
    _path: str = tmp_path / "test.txt"

    ParserXml.write(_path, settings.TEST_LINES_XML)

    assert filecmp.cmp(path, _path)


def test_write_vtt(tmp_path):
    path: str = glob.glob(f"{settings.TEST_DATA_DIR}/vtt2txt/write.txt")[0]
    _path: str = tmp_path / "test.txt"

    ParserVtt.write(_path, settings.TEST_LINES_VTT)

    assert filecmp.cmp(path, _path)
