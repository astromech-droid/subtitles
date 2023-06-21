import re

from app.utils import downloader, filter, loader, parser_vtt, parser_xml, sender


def download_vtt(url, dirname):
    return downloader.download_segments(url, dirname)


def download_xml(url, path):
    return downloader.download_subs(url, path)


def load_subs(path, title):
    loader.load_subs(path, title)


def reload_subs(path, title):
    loader.reload_subs(path, title)


def read_lines(path):
    extension = re.match(r".*\.(\w+)$", path)[1]  # Ex. vtt, xml

    if extension == "vtt":
        lines = parser_vtt.parse_vtt(path)

    elif extension == "xml":
        lines = parser_xml.parse_xml(path)

    lines = filter.merge(lines)

    return lines


def send_lines(url, lines):
    sender.send_lines(url, lines)
