import json

from app.models import Episode, Line
from app.tests import settings
from django.test import TestCase
from django.urls import reverse


class WordguesserApiTestCase(TestCase):
    def setUp(self):
        title = settings.TEST_VTT_EPISODE_TITLE
        episode = Episode.objects.create(title=title)
        lines = settings.TEST_WORDGUESSER_IGNORED

        for i, line in enumerate(lines, 1):
            timestamp, text = line
            line = Line.objects.create(
                episode=episode, timestamp=timestamp, text=text, line_number=i
            )

    def test_ignore(self):
        url = reverse("wordguesser_api")
        response = self.client.get(url)
        line = json.loads(response.content)["line"]
        self.assertEqual(line, {})

    def tearDown(self):
        pass
