from subtitles.Downloader import Downloader


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

    def read(self):
        pass
