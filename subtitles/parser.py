import os

from subtitles import vtt2txt, xml2txt
from subtitles.conf import settings


class Parser:
    def __init__(self, service: str, title: str):
        if service == settings.SERVICE_DISNEYPLUS:
            self.core = vtt2txt
            self.dirname_src: str = os.path.join(settings.VTT_DIR, title)

        elif service == settings.SERVICE_NETFLIX:
            self.core = xml2txt
            self.dirname_src: str = os.path.join(settings.XML_DIR, title)

        self.dirname_dst: str = os.path.join(settings.TXT_DIR, title)

    def parse(self, lines: list[str]) -> list[tuple[str]]:
        return self.core.parse(lines)

    def read(self, path: str) -> list[str]:
        return self.core.read(path)

    def write(self, path: str, lines: list[tuple[str]]) -> None:
        dirname: str = os.path.dirname(path)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(path, "w") as f:
            for starttime, text in lines:
                f.write(f"{starttime}: {text}\n")
