import math
import re

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


def parse(path: str) -> list[tuple[str]]:
    with open(path, "r", encoding="utf-8-sig") as f:
        xml_doc: str = f.read()

    lines: list[tuple[str]] = []

    soup = BeautifulSoup(xml_doc, "xml")
    elements = list(soup.find_all("p"))  # NavigableString, Tag

    for el in elements:
        starttime: str = _get_starttime(el)
        text: str = _get_text(el)
        line: tuple[str] = (starttime, text)
        lines.append(line)

    return lines


def _get_starttime(element) -> str:
    starttime: str = element.get("begin")  # ex. 8050000000t
    seconds: float = int(re.match(r"^(\d+)t", starttime)[1]) / 10000000

    h = math.floor(seconds / 3600)
    m = math.floor(seconds / 60 - (h * 60))
    s = math.floor(seconds - (h * 3600 + m * 60))
    ms = "{:.3f}".format(seconds - math.floor(seconds))[2:]

    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}.{ms}"


def _get_text(element) -> str:
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