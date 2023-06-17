from app.tests import settings
from app.utils import parse_xml
from django.test import TestCase


class ParserTestCase(TestCase):
    def test_parse_xml(self):
        path = settings.TEST_XML_PATH
        lines: list[tuple[str]] = parse_xml.parse(path)
        self.assertEqual(lines, settings.TEST_XML_VALUE)
