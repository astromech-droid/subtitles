import os
import re
import time

import requests

from cli.conf import settings
from cli.exceptions import NotFound


class Downloader:
    def __init__(self, service: str, title: str):
        self.service = service
        self.title = title

        if self.service == settings.SERVICE_DISNEYPLUS:
            self.dirname: str = os.path.join(settings.VTT_DIR, title)

        elif self.service == settings.SERVICE_NETFLIX:
            self.dirname: str = os.path.join(settings.XML_DIR, title)

    def _fetch(self, url: str) -> str:
        response = requests.get(url)

        if response.status_code == 404:
            raise NotFound

        return response.text

    def _save(self, text: str, path: str) -> None:
        dirname: str = os.path.dirname(path)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

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
        try:
            text: str = self._fetch(url)
            self._save(text, path)

        except NotFound:
            raise NotFound

    def download_all(self, urls: list[str], dirname: str) -> list[str]:
        pathes: list[str] = []

        for url in urls:
            if self.service == settings.SERVICE_DISNEYPLUS:
                filename: str = re.match(r"^https://.*/(seg.*.vtt)$", url)[1]

            elif self.service == settings.SERVICE_NETFLIX:
                filename: str = settings.DEFAULT_XML_FILENAME

            try:
                path: str = os.path.join(dirname, filename)
                self.download(url, path)
            except NotFound:
                break

            pathes.append(path)
            time.sleep(settings.DOWNLOAD_INTERVAL)

        return pathes
