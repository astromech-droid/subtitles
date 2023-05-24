import glob
import os

from subtitles import vtt2txt
from subtitles.conf import settings

title: str = "zootopia_plus_s1e1"
dirname: str = os.path.join(settings.VTT_DIR, title)

pathes: list[str] = glob.glob(f"{dirname}/*")
path: str = pathes[0]
lines: list[list[str]] = vtt2txt.read(path)

for starttime, text in lines:
    print(f"{starttime}: {text}")


# Usage - xml2txt -
"""
import glob
import os

from subtitles import xml2txt
from subtitles.conf import settings

title: str = "kid_cosmic_s1e1"
dirname: str = os.path.join(settings.XML_DIR, title)

pathes: list[str] = glob.glob(f"{dirname}/*")
path: str = pathes[0]
lines: list[list[str]] = xml2txt.read(path)

for starttime, text in lines:
    print(f"{starttime}: {text}")
"""


# Usage - download -
"""
from subtitles.conf import settings
from subtitles.Downloader import Downloader

service = settings.SERVICE_DISNEYPLUS
downloader = Downloader(service)
title = "test"

url: str = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/e6a5d957-222a-485b-974a-1cdb3e9295a9/r/1bf93eac-71ed-4039-a071-3ade818c6fd6/4b9e-MAIN/06/subtitles_1/seg_00000.vtt"
urls: list[str] = downloader.get_urls(url)
dirname: str = downloader.get_dirname(title)

downloader.download_all(urls, dirname)
"""
