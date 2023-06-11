import os

from cli.conf import settings
from cli.core.vtt2txt import Vtt2txt
from cli.core.xml2txt import Xml2txt


class Parser:
    def __init__(self, service: str, title: str):
        if service == settings.SERVICE_DISNEYPLUS:
            self.core = Vtt2txt()
            self.dirname_src: str = os.path.join(settings.VTT_DIR, title)

        elif service == settings.SERVICE_NETFLIX:
            self.core = Xml2txt()
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
