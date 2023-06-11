from cli.downloader import Downloader
from cli.parser import Parser


class Subtitles:
    def __init__(self, service: str, title: str):
        self.service = service
        self.title = title
        self.downloader = Downloader(self.service, self.title)
        self.parser = Parser(self.service, self.title)

    def download(self, url: str):
        urls: list[str] = self.downloader.get_urls(url)
        dirname: str = self.downloader.dirname
        pathes: list[str] = self.downloader.download_all(urls, dirname)

        return pathes

    def read(self, path: str) -> list[tuple[str]]:
        return self.parser.read(path)

    def write(self, path: str, lines: list[tuple[str]]) -> None:
        return self.parser.write(path, lines)
