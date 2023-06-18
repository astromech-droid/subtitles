import filecmp
import os
import shutil

from app.tests import settings
from app.utils import downloader, filter, parser_vtt, parser_xml
from django.test import TestCase


class ParseXmlTestCase(TestCase):
    def test_parse_xml(self):
        path = settings.TEST_XML_PATH
        lines: list[tuple[str]] = parser_xml.parse_xml(path)
        self.assertEqual(lines, settings.TEST_XML_VALUE)


class ParseVttTestCase(TestCase):
    def test_parse_vtt(self):
        path = settings.TEST_VTT_PATH
        lines: list[tuple[str]] = parser_vtt.parse_vtt(path)
        self.assertEqual(lines, settings.TEST_VTT_VALUE)


class DownloadSubsTestCase(TestCase):
    def setUp(self):
        self.tmp_path = os.path.join(settings.TEST_TMP_DIR, "test.vtt")
        if not os.path.exists(settings.TEST_TMP_DIR):
            os.makedirs(settings.TEST_TMP_DIR)

    def test_download_subs(self):
        url = settings.TEST_VTT_URL
        path = downloader.download_subs(url, self.tmp_path)
        self.assertEqual(filecmp.cmp(path, settings.TEST_VTT_PATH), True)

    def test_download_segments(self):
        url = settings.TEST_SEGMENT_URLS[0]
        pathes = downloader.download_segments(url, settings.TEST_TMP_DIR)
        for i, path in enumerate(pathes):
            self.assertEqual(filecmp.cmp(path, settings.TEST_SEGMENT_PATHES[i]), True)

    def tearDown(self):
        tmp_dir = os.path.dirname(self.tmp_path)
        shutil.rmtree(tmp_dir)


class FilterTestCase(TestCase):
    def test_merge(self):
        lines = settings.TEST_FILTER_VALUE["before"]
        _lines = filter.merge(lines)
        self.assertEqual(_lines, settings.TEST_FILTER_VALUE["after"])
