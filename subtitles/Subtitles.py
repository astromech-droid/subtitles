import re

from subtitles.conf import settings
from subtitles.engines.Vtt2txt import Vtt2txt
from subtitles.engines.Xml2txt import Xml2txt
from subtitles.engines.Xxx2txt import Xxx2txt


class Subtitles:
    def __init__(self):
        pass

    def _get_engine(self, url: str) -> Xxx2txt:
        if re.match(settings.TEST_XML_URL, url):
            return Xml2txt

        elif re.match(settings.TEST_VTT_URL, url):
            return Vtt2txt

        else:
            return None

    def run(self, url: str, title: str) -> list:
        engine = self._get_engine(url)

        if engine is None:
            raise Exception("UnknownURL: Engine Not Found")

        pathes = engine(title).run(url)

        return pathes
