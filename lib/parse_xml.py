import math
import os
import re

import settings as s
from bs4 import BeautifulSoup

from .parse_vtt import merge_multilines


def to_int(starttime: str) -> int:
    st = re.match(r"(\d*)t", starttime)[1]
    return int(st)


def to_formatted_time(seconds: float) -> str:
    h = math.floor(seconds / 3600)
    m = math.floor(seconds / 60)
    s = math.floor(seconds - (h * 3600 + m * 60))
    ms = "{:.3f}".format(seconds - math.floor(seconds))[2:]
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}.{ms}"


def parse(lines: list) -> list:
    xml_doc = "".join(lines)
    soup = BeautifulSoup(xml_doc, "xml")
    new_lines = []

    for line in soup.find_all("p"):
        seconds: float = to_int(line.get("begin")) / 10000000
        starttime = to_formatted_time(seconds)
        contents_str = []
        for c in line.contents:
            if c.text != "":
                contents_str.append(c.text)

        text = " ".join(contents_str)
        new_lines.append(f"{starttime}: {text}\n")

    return new_lines


def parse_and_save(dirname, service):
    if service == s.Service.NETFLIX:
        xml_dir = os.path.join(s.XML_DIR, dirname)
        txt_dir = os.path.join(s.TXT_DIR, dirname)

        xml_path = os.path.join(xml_dir, "subtitle.xml")
        out_path = os.path.join(txt_dir, "subtitle.txt")

        if not os.path.exists(txt_dir):
            os.makedirs(txt_dir)

        with open(xml_path, "r") as f_input:
            lines = parse(f_input.readlines())
            lines = merge_multilines(lines)

        with open(out_path, "w") as f_output:
            f_output.writelines(lines)
