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

    def _parse_subtitles(self, from_path: str, to_path: str) -> bool:
        lines: list = files.get_lines(from_path)
        lines = self._parse_lines(lines)
        result: bool = files.save_lines(lines, to_path)
        return result

    def _download_all_subtitles(self, url: str) -> list:
        urls: list = http.get_urls(url, self.service)
        pathes: list = http.download_all_subtitles(urls, self.dirname, self.service)
        return pathes

    def _parse_all_subtitles(self, pathes: list, title: str) -> list:
        to_pathes = []

        for path in pathes:
            dirname: str = os.path.join(settings.TXT_DIR, title)

            if self.service == settings.SERVICE_DISNEYPLUS:
                filename: str = re.match(r"^.*/(.*)\.\w+$", path)[1] + ".txt"
            elif self.service == settings.SERVICE_NETFLIX:
                filename: str = settings.DEFAULT_TXT_FILENAME

            to_path: str = os.path.join(dirname, filename)

            if self._parse_subtitles(from_path=path, to_path=to_path):
                to_pathes.append(to_path)

            else:
                break

        return to_pathes

    def run(self, url: str) -> list:
        pathes = self._download_all_subtitles(url)
        to_pathes = self._parse_all_subtitles(pathes, self.title)

        return to_pathes
