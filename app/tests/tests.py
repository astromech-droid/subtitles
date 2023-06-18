import filecmp
import os
import shutil

from app.tests import settings
from app.utils import downloader, filter, loader, parser_vtt, parser_xml
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
    def test_merge_vtt(self):
        lines = settings.TEST_VTT_VALUE
        _lines = filter.merge(lines)
        self.assertEqual(_lines, settings.TEST_VTT_FILTERED_VALUE)

    def test_merge_xml(self):
        lines = settings.TEST_XML_VALUE
        _lines = filter.merge(lines)
        self.assertEqual(_lines, settings.TEST_XML_FILTERED_VALUE)


class LoaderTestCase(TestCase):
    def load_subs(self, title, path, filtered_value):
        lines = loader.load_subs(path, title)

        for i, line in enumerate(lines):
            timestamp, text = filtered_value[i]
            self.assertEqual(line.timestamp, timestamp)
            self.assertEqual(line.text, text)
            self.assertEqual(line.episode.title, title)
            self.assertEqual(line.line_number, i + 1)

    def test_load_subs_vtt(self):
        title = settings.TEST_VTT_EPISODE_TITLE
        path = settings.TEST_VTT_PATH
        filtered_value = settings.TEST_VTT_FILTERED_VALUE
        self.load_subs(title, path, filtered_value)

    def test_load_subs_xml(self):
        title = settings.TEST_XML_EPISODE_TITLE
        path = settings.TEST_XML_PATH
        filtered_value = settings.TEST_XML_FILTERED_VALUE
        self.load_subs(title, path, filtered_value)
