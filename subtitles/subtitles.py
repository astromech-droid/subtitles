from subtitles import vtt2txt, xml2txt
from subtitles.conf import settings
from subtitles.downloader import Downloader


class Subtitles:
    def __init__(self, service: str, title: str):
        self.service = service
        self.title = title

    def download(self, url: str):
        downloader = Downloader(self.service)
        urls: list[str] = downloader.get_urls(url)

        dirname: str = downloader.get_dirname(self.title)
        pathes: list[str] = downloader.download_all(urls, dirname)

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
