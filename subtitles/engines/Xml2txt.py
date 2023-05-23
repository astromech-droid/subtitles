from subtitles.conf import settings
from subtitles.engines.Xxx2txt import Xxx2txt
from subtitles.utils import parsers


class Xml2txt(Xxx2txt):
    def __init__(self, title: str) -> None:
        self.service = settings.SERVICE_NETFLIX
        super().__init__(title, self.service)

    def _parse_lines(self, lines: list) -> list:
        new_lines = []

        for element in parsers.extruct_elements(lines):
            starttime: str = parsers.get_starttime(element)
            text: str = parsers.get_text(element)
            new_lines.append(f"{starttime}: {text}\n")

        new_lines: list = parsers.merge_multilines(new_lines)

        return new_lines
