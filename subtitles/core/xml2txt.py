import math
import os
import re

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from subtitles.conf import settings as s
from subtitles.utils import files, http, parsers


def _to_int(starttime: str) -> int:
    st = re.match(r"(\d*)t", starttime)[1]
    return int(st)


def _to_formatted_time(seconds: float) -> str:
    h = math.floor(seconds / 3600)
    m = math.floor(seconds / 60)
    s = math.floor(seconds - (h * 3600 + m * 60))
    ms = "{:.3f}".format(seconds - math.floor(seconds))[2:]
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}.{ms}"


def _get_texts_recurse(line) -> list:
    texts = []
    for c in line.contents:
        if type(c) is NavigableString:
            if c.text != "":
                texts.append(c.text)

        elif type(c) is Tag:
            if c.text != "":
                text = " ".join(_get_texts_recurse(c))
                texts.append(text)

        else:
            print("## ERROR ##")

    return texts


def parse_lines(lines: list) -> list:
    xml_doc = "".join(lines)
    soup = BeautifulSoup(xml_doc, "xml")
    new_lines = []

    for line in soup.find_all("p"):
        seconds: float = _to_int(line.get("begin")) / 10000000
        starttime = _to_formatted_time(seconds)
        texts = _get_texts_recurse(line)
        text = " ".join(texts)
        new_lines.append(f"{starttime}: {text}\n")

    new_lines: list = parsers.merge_multilines(new_lines)

    return new_lines


def parse_subtitles(from_path: str, to_path: str) -> bool:
    lines: list = files.get_lines(from_path)
    lines: list = parse_lines(lines)

    result: bool = files.save_lines(lines, to_path)

    return result


def download_all_subtitles(url: str, title: str, service: str) -> list:
    dirname: str = os.path.join(s.XML_DIR, title)
    urls: list = http.get_urls(url, service)
    pathes: list = http.download_all_subtitles(urls, dirname, service)
    return pathes


def parse_all_subtitles(pathes: list, title: str) -> list:
    to_pathes = []

    for path in pathes:
        dirname: str = os.path.join(s.TXT_DIR, title)
        filename = s.DEFAULT_TXT_FILENAME
        to_path: str = os.path.join(dirname, filename)

        if parse_subtitles(from_path=path, to_path=to_path):
            to_pathes.append(to_path)

        else:
            break

    return to_pathes


def run(url: str, title: str, service: str) -> list:
    pathes = download_all_subtitles(url, title, service)
    to_pathes = parse_all_subtitles(pathes, title)

    return to_pathes
