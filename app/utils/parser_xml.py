import math
import re

from bs4 import BeautifulSoup


def parse_xml(path: str) -> list[tuple[str]]:
    with open(path, "r", encoding="utf-8-sig") as f:
        xml_doc: str = f.read()

    lines: list[tuple[str]] = []

    soup = BeautifulSoup(xml_doc, "xml")
    elements = list(soup.find_all("p"))  # NavigableString, Tag

    for el in elements:
        starttime: str = _get_starttime(el)
        texts: list[str] = _get_texts(el)
        for text in texts:
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


def _get_texts(element) -> list[str]:
    def _recurse(element) -> list[str]:
        texts: list[str] = []
        text: str = ""

        for i, content in enumerate(element.contents, 1):
            if content.name == "span":
                _texts = _recurse(content)
                text += str(" ").join(_texts)

            elif content.name == "br":
                texts.append(text)
                text = ""

            elif content.name is None:
                text += content.text

            if i == len(element.contents):
                texts.append(text)
                text = ""

        return texts

    return _recurse(element)
