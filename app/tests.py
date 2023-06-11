import glob

from django.test import TestCase
from subtitles import settings

from app.models import Episode


class EpisodeTestCase(TestCase):
    def test_import(self):
        title = "test_s1e1"
        episode = Episode.objects.create(title=title)
        path = glob.glob(f"{settings.TEST_DATA_DIR}/importer/{title}/subtitles.txt")[0]
        lines = episode.import_txt(path)

        for i, line in enumerate(lines):
            self.assertEqual(line.episode.title, title)
            self.assertEqual(line.line_number, settings.TEST_DATABASE_TXT[i][0])
            self.assertEqual(line.timestamp, settings.TEST_DATABASE_TXT[i][1])
            self.assertEqual(line.text, settings.TEST_DATABASE_TXT[i][2])
