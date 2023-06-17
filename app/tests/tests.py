from app.tests import settings
from app.utils import parse_vtt, parse_xml
from django.test import TestCase


class ParseXmlTestCase(TestCase):
    def test_parse_xml(self):
        path = settings.TEST_XML_PATH
        lines: list[tuple[str]] = parse_xml.parse(path)
        self.assertEqual(lines, settings.TEST_XML_VALUE)


class ParseVttTestCase(TestCase):
    def test_parse_vtt(self):
        path = settings.TEST_VTT_PATH
        lines: list[tuple[str]] = parse_vtt.parse(path)
        self.assertEqual(lines, settings.TEST_VTT_VALUE)
