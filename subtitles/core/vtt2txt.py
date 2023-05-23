import os
import re

from subtitles.conf import settings as s
from subtitles.utils import files, http, parsers


def parse_lines(lines: list) -> list:
    lines = parsers.remove_linenumbers(lines)
    lines = parsers.remove_headers(lines)
    lines = parsers.remove_blanklines(lines)
    lines = parsers.extruct_starttime(lines)
    lines = parsers.put_starttime_on_alllines(lines)
    lines = parsers.merge_multilines(lines)
    return lines


def parse_subtitles(from_path: str, to_path: str) -> bool:
    lines: list = files.get_lines(from_path)
    lines = parse_lines(lines)

    result: bool = files.save_lines(lines, to_path)
    return result


def download_all_subtitles(url: str, title: str, service: str) -> list:
    dirname: str = os.path.join(s.VTT_DIR, title)
    urls: list = http.get_urls(url, service)
    pathes: list = http.download_all_subtitles(urls, dirname, service)
    return pathes


def parse_all_subtitles(pathes: list, title: str) -> list:
    to_pathes = []

    for path in pathes:
        dirname: str = os.path.join(s.TXT_DIR, title)
        filename = re.match(r"^.*/(.*)\.\w+$", path)[1] + ".txt"
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
