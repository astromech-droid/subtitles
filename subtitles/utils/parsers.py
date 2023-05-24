import copy
import math
import re

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


def remove_linenumbers(lines: list) -> list:
    new_lines = []

    for line in lines:
        if not re.match(r"^\d+\n$", line):
            new_lines.append(line)

    return new_lines


def remove_headers(lines: list) -> list:
    for line in copy.copy(lines):
        starttime = re.match(r"(^\d{2}:\d{2}:\d{2}.\d{3}) -->.*", line)

        if starttime is None:
            lines.pop(0)

        else:
            break

    return lines


def remove_blanklines(lines: list) -> list:
    new_lines = []

    for line in lines:
        if not line == "\n":
            new_lines.append(line)

    return new_lines


def extruct_starttime(lines: list) -> list:
    new_lines = []

    for line in lines:
        starttime = re.match(r"(^\d{2}:\d{2}:\d{2}.\d{3}) -->.*", line)

        if starttime is None:
            new_lines.append(line)
        else:
            new_lines.append(starttime[1] + "\n")

    return new_lines


def put_starttime_on_alllines(lines: list) -> list:
    new_lines = []
    queue = []

    for line in lines:
        starttime = re.match(r"(^\d{2}:\d{2}:\d{2}.\d{3}).*", line)

        if starttime is None:
            new_lines.append(f"{queue[0]}: {line}")

        else:
            queue.clear()
            queue.append(starttime[1])

    return new_lines


def merge_multilines(lines: list) -> list:
    starttime_queue = []
    text_queue = []
    new_lines = []

    for line in lines:
        _line = re.match(r"(^\d{2}:\d{2}:\d{2}.\d{3}): (.*)\n", line)

        if _line is not None:
            starttime = _line[1]
            text = _line[2]

            text_queue.append(text)

            if len(starttime_queue) == 0:
                starttime_queue.append(starttime)

            if re.match(r"(.*\w$|.*,$)", text_queue[len(text_queue) - 1]) is None:
                new_lines.append(f"{starttime_queue[0]}: {str(' ').join(text_queue)}\n")
                starttime_queue.clear()
                text_queue.clear()

    return new_lines


def extruct_elements(lines: list) -> list:
    xml_doc = "".join(lines)
    soup = BeautifulSoup(xml_doc, "xml")
    elements = list(soup.find_all("p"))  # NavigableString, Tag

    return elements


def _to_int(starttime: str) -> int:
    st = re.match(r"(\d*)t", starttime)[1]
    return int(st)


def _get_seconds(element: Tag) -> float:
    seconds: float = _to_int(element.get("begin")) / 10000000
    return seconds


def _to_time_str(seconds: float) -> str:
    h = math.floor(seconds / 3600)
    m = math.floor(seconds / 60)
    s = math.floor(seconds - (h * 3600 + m * 60))
    ms = "{:.3f}".format(seconds - math.floor(seconds))[2:]
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}.{ms}"


def get_starttime(element: Tag) -> str:
    seconds: float = _get_seconds(element)
    starttime = _to_time_str(seconds)

    return starttime


def _get_texts_recursively(element) -> list:
    texts = []
    for c in element.contents:
        if type(c) is NavigableString:
            if c.text != "":
                texts.append(c.text)

        elif type(c) is Tag:
            if c.text != "":
                text = " ".join(_get_texts_recursively(c))
                texts.append(text)

        else:
            print("## ERROR ##")

    return texts


def get_text(element: Tag) -> str:
    texts = _get_texts_recursively(element)
    return " ".join(texts)
