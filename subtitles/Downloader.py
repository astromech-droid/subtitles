import os
import re
import time

import requests

from subtitles.conf import settings


class Downloader:
    def __init__(self, service: str):
        self.service = service
        pass

    def _fetch(self, url: str) -> str:
        response = requests.get(url)
        return response.text

    def _save(self, text: str, path: str) -> None:
        with open(path, "w") as f:
            f.write(text)

    def get_urls(self, url: str) -> list[str]:
        urls = []

        if self.service == settings.SERVICE_DISNEYPLUS:
            for i in range(0, settings.MAX_SEGMENTS):
                url_head = re.match(r"(^https://.*/)seg_\d{5}.vtt", url)[1]
                seg_filename = f"seg_{str(i).zfill(5)}.vtt"
                urls.append(f"{url_head}{seg_filename}")

        elif self.service == settings.SERVICE_NETFLIX:
            urls.append(url)

        return urls

    def download(self, url: str, path: str) -> None:
        text: str = self._fetch(url)
        self._save(text, path)

    def get_dirname(self, title: str) -> str:
        if self.service == settings.SERVICE_DISNEYPLUS:
            dirname: str = os.path.join(settings.VTT_DIR, title)

        elif self.service == settings.SERVICE_NETFLIX:
            dirname: str = os.path.join(settings.XML_DIR, title)

        return dirname

    def download_all(self, urls: list[str], dirname: str) -> list[str]:
        pathes: list[str] = []

        for url in urls:
            if self.service == settings.SERVICE_DISNEYPLUS:
                filename: str = re.match(r"^https://.*/(seg.*.vtt)$", url)[1]

            elif self.service == settings.SERVICE_NETFLIX:
                filename: str = settings.DEFAULT_XML_FILENAME

            path: str = os.path.join(dirname, filename)
            self.download(url, path)
            pathes.append(path)

            time.sleep(0.5)

        return pathes
