from app.utils import downloader


def download_vtt(url, dirname):
    downloader.download_segments(url, dirname)


def download_xml(url, path):
    downloader.download_subs(url, path)
