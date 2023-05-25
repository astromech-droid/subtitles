from subtitles import vtt2txt, xml2txt
from subtitles.conf import settings
from subtitles.downloader import Downloader


class Subtitles:
    def __init__(self, service: str, title: str):
        self.service = service
        self.title = title
        self.downloader = Downloader(self.service, self.title)

    def download(self, url: str):
        urls: list[str] = self.downloader.get_urls(url)
        dirname: str = self.downloader.dirname
        pathes: list[str] = self.downloader.download_all(urls, dirname)

        return pathes

    def read(self, path: str) -> list[tuple[str]]:
        if self.service == settings.SERVICE_DISNEYPLUS:
            return vtt2txt.read(path)

        elif self.service == settings.SERVICE_NETFLIX:
            return xml2txt.read(path)

    def write(self, path: str, lines: list[tuple[str]]) -> None:
        if self.service == settings.SERVICE_DISNEYPLUS:
            return vtt2txt.write(path, lines)

        elif self.service == settings.SERVICE_NETFLIX:
            return xml2txt.write(path, lines)
