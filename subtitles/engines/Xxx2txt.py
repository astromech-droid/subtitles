import os
import re

from subtitles.conf import settings
from subtitles.utils import files, http


class Xxx2txt:
    def __init__(self, title: str, service: str) -> None:
        self.title = title
        self.service = service

        if self.service == settings.SERVICE_DISNEYPLUS:
            self.dirname: str = os.path.join(settings.VTT_DIR, title)

        elif self.service == settings.SERVICE_NETFLIX:
            self.dirname: str = os.path.join(settings.XML_DIR, title)

    def _parse_lines(self, lines: list) -> list:
        pass

    def _parse_subtitles(self, path_src: str, path_dst: str) -> bool:
        lines: list = files.get_lines(path_src)
        lines = self._parse_lines(lines)
        result: bool = files.save_lines(lines, path_dst)
        return result

    def download_all_subtitles(self, url: str) -> list:
        urls: list = http.get_urls(url, self.service)
        pathes: list = http.download_all_subtitles(urls, self.dirname, self.service)
        return pathes

    def parse_all_subtitles(self, pathes: list) -> list:
        pathes_dst = []

        for path_src in pathes:
            dirname: str = os.path.join(settings.TXT_DIR, self.title)

            if self.service == settings.SERVICE_DISNEYPLUS:
                filename: str = re.match(r"^.*/(.*)\.\w+$", path_src)[1] + ".txt"
            elif self.service == settings.SERVICE_NETFLIX:
                filename: str = settings.DEFAULT_TXT_FILENAME

            path_dst: str = os.path.join(dirname, filename)

            if self._parse_subtitles(path_src, path_dst):
                pathes_dst.append(path_dst)

            else:
                break

        return pathes_dst
