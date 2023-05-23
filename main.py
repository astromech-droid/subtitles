import os
import re

from subtitles.conf import settings as s
from subtitles.core import vtt2txt, xml2txt
from subtitles.utils import http


def main(url: str, title: str, service: str):
    if service == s.SERVICE_DISNEYPLUS:
        dir: str = s.VTT_DIR

    elif service == s.SERVICE_NETFLIX:
        dir: str = s.XML_DIR

    # Download Subtitles
    dirname: str = os.path.join(dir, title)
    urls: list = http.get_urls(url, service)
    pathes: list = http.download_all_subtitles(urls, dirname, service)
    to_pathes: list = []

    # Parse Subtitles
    for path in pathes:
        dirname_txt: str = os.path.join(s.TXT_DIR, title)

        if service == s.SERVICE_DISNEYPLUS:
            filename = re.match(r"^.*/(.*)\.\w+$", path)[1] + ".txt"
            to_path: str = os.path.join(dirname_txt, filename)
            parse_subtitles = vtt2txt.parse_subtitles

        if service == s.SERVICE_NETFLIX:
            filename = s.DEFAULT_TXT_FILENAME
            to_path: str = os.path.join(dirname_txt, filename)
            parse_subtitles = xml2txt.parse_subtitles

        if parse_subtitles(from_path=path, to_path=to_path):
            to_pathes.append(to_path)

        else:
            break

    return to_pathes


# DisneyPlus: vtt
url: str = "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils/http/vtt/seg_00000.vtt"
title: str = "disneyplus_s1e1"
service: str = s.SERVICE_DISNEYPLUS
# service: str = s.SERVICE_NETFLIX

pathes = main(url, title, service)
for path in pathes:
    print(path)
