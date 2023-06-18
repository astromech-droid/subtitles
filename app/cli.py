from app.utils import downloader, importer


def download_vtt(url, dirname):
    return downloader.download_segments(url, dirname)


def download_xml(url, path):
    return downloader.download_subs(url, path)


def import_subs(path, title):
    importer.import_subs(path, title)
