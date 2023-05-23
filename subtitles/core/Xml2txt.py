from bs4 import BeautifulSoup
from subtitles.conf import settings
from subtitles.core.Xxx2txt import Xxx2txt
from subtitles.utils import parsers


class Xml2txt(Xxx2txt):
    def __init__(self, title: str) -> None:
        self.service = settings.SERVICE_NETFLIX
        super().__init__(title, self.service)

    def _parse_lines(self, lines: list) -> list:
        xml_doc = "".join(lines)
        soup = BeautifulSoup(xml_doc, "xml")
        new_lines = []

        for line in soup.find_all("p"):
            seconds: float = parsers.to_int(line.get("begin")) / 10000000
            starttime = parsers.to_formatted_time(seconds)
            texts = parsers.get_texts_recurse(line)
            text = " ".join(texts)
            new_lines.append(f"{starttime}: {text}\n")

        new_lines: list = parsers.merge_multilines(new_lines)

        return new_lines
