import os
import re

from subtitles.core import filters
from subtitles.core.xxx2txt import Xxx2txt


class Vtt2txt(Xxx2txt):
    def __init__(self):
        pass

    def parse(self, lines: list[str]) -> list[tuple[str]]:
        _lines: list[tuple[str]] = []
        text_buffer: list[str] = []
        starttime_buffer: str = ""

        for line in lines:
            match_st: re.Match = re.match(r"^(\d{2}:\d{2}:\d{2}.\d{3}) -->.*", line)

            if match_st:
                starttime: str = match_st[1]

                if starttime_buffer == "":
                    text_buffer.clear()

                else:
                    _lines.append((starttime_buffer, " ".join(text_buffer)))
                    text_buffer.clear()

                starttime_buffer = starttime

            else:
                match_txt: re.Match = re.match(r"(.+)\n", line)
                if match_txt:
                    text: str = match_txt[1]
                    text_buffer.append(text)

        _lines.append((starttime_buffer, " ".join(text_buffer)))

        return filters.merge(_lines)

    def read(self, path: str) -> list[str]:
        with open(path, "r", encoding="utf-8-sig") as f:
            lines: list[str] = f.readlines()

        return self.parse(lines)

    def write(self, path: str, lines: list[tuple[str]]) -> None:
        dirname: str = os.path.dirname(path)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(path, "w") as f:
            for starttime, text in lines:
                f.write(f"{starttime}: {text}\n")
