from app.utils import downloader, loader


def download_vtt(url, dirname):
    return downloader.download_segments(url, dirname)


def download_xml(url, path):
    return downloader.download_subs(url, path)


def load_subs(path, title):
    loader.load_subs(path, title)
