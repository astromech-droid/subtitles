import math
import os
import re

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from cli.core import filters
from cli.core.xxx2txt import Xxx2txt


class Xml2txt(Xxx2txt):
    def __init__(self):
        pass

    def _get_starttime(self, element) -> str:
        starttime: str = element.get("begin")  # ex. 8050000000t
        seconds: float = int(re.match(r"^(\d+)t", starttime)[1]) / 10000000

        h = math.floor(seconds / 3600)
        m = math.floor(seconds / 60)
        s = math.floor(seconds - (h * 3600 + m * 60))
        ms = "{:.3f}".format(seconds - math.floor(seconds))[2:]

        return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}.{ms}"

    def _get_text(self, element) -> str:
        def __recurse(element) -> list[str]:
            _text: list[str] = []

            for c in element.contents:
                if type(c) is NavigableString:
                    if c.text != "":
                        _text.append(c.text)

                elif type(c) is Tag:
                    if c.text != "":
                        _: str = " ".join(__recurse(c))
                        _text.append(_)

            return _text

        text: list[str] = __recurse(element)

        return " ".join(text)

    def parse(self, xml_doc: str) -> list[tuple[str]]:
        lines: list[tuple[str]] = []

        soup = BeautifulSoup(xml_doc, "xml")
        elements = list(soup.find_all("p"))  # NavigableString, Tag

        for el in elements:
            starttime: str = self._get_starttime(el)
            text: str = self._get_text(el)
            line: tuple[str] = (starttime, text)
            lines.append(line)

        return filters.merge(lines)

    def read(self, path: str) -> list[str]:
        with open(path, "r", encoding="utf-8-sig") as f:
            xml_doc: str = f.read()

        return self.parse(xml_doc)

    def write(self, path: str, lines: list[tuple[str]]) -> None:
        dirname: str = os.path.dirname(path)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(path, "w") as f:
            for starttime, text in lines:
                f.write(f"{starttime}: {text}\n")