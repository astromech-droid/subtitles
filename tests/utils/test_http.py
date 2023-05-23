import settings as s

from utils import files, http


def test_download_subtitles_save(tmp_path):
    filename: str = "download_subtitles.txt"
    path: str = files.find_path(s.TEST_DATA_DIR, filename)
    url: str = f"https://raw.githubusercontent.com/astromech-droid/subtitles/main/{path}"

    http.download_subtitles(url, tmp_path / filename)
    expected: list = files.get_lines(path)

    assert files.get_lines(tmp_path / filename) == expected


def test_download_subtitles_true(tmp_path):
    filename: str = "download_subtitles.txt"
    path: str = files.find_path(s.TEST_DATA_DIR, filename)
    url: str = f"https://raw.githubusercontent.com/astromech-droid/subtitles/main/{path}"

    assert http.download_subtitles(url, tmp_path / filename) is True


def test_download_subtitles_false(tmp_path):
    filename: str = "doesntexists.txt"
    url: str = "https://raw.githubusercontent.com/astromech-droid/doesntexists"

    assert http.download_subtitles(url, tmp_path / filename) is False


def test_get_urls_disneyplus():
    url: str = "https://test.com/subtitles/seg_00000.vtt"
    path: str = files.find_path(s.TEST_DATA_DIR, "get_urls.txt")

    expected: list = files.get_lines(path)
    expected: list = [x.strip() for x in expected]  # remove new line characters

    assert http.get_urls(url, s.SERVICE_DISNEYPLUS) == expected


def test_get_urls_netflix():
    url: str = "https://test.com/subtitles/seg_00000.vtt"

    assert http.get_urls(url, s.SERVICE_NETFLIX) == [url]


def test_download_all_subtitles(tmp_path):
    url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/cca28bc2-eb49-476a-af99-173d06cfafc8/r/bf6f3bfc-01e1-4270-b605-264de963aab0/3737-MAIN/06/subtitles_1/seg_00001.vtt"
    urls = http.get_urls(url, s.SERVICE_DISNEYPLUS)

    dirname = tmp_path
    expected: list = ["seg_00000.vtt", "seg_00001.vtt"]

    assert http.download_all_subtitles(urls, dirname) == expected
