from subtitles.conf import settings
from subtitles.engines.Xxx2txt import Xxx2txt
from subtitles.utils import parsers


class Vtt2txt(Xxx2txt):
    def __init__(self, title: str) -> None:
        self.service = settings.SERVICE_DISNEYPLUS

        super().__init__(title, self.service)

    def _parse_lines(self, lines: list) -> list:
        lines = parsers.remove_linenumbers(lines)
        lines = parsers.remove_headers(lines)
        lines = parsers.remove_blanklines(lines)
        lines = parsers.extruct_starttime(lines)
        lines = parsers.put_starttime_on_alllines(lines)
        lines = parsers.merge_multilines(lines)
        return lines
