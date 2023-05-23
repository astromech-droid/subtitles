import os
import re

import conf.settings as s
from core import vtt2txt, xml2txt
from utils import http


def main(url: str, title: str, service: str):
    if service == s.SERVICE_DISNEYPLUS:
        # Download Subtitles
        dirname: str = os.path.join(s.VTT_DIR, title)
        urls: list = http.get_urls(url, service)
        pathes: list = http.download_all_subtitles(urls, dirname, service)

        # Parse Subtitles
        for path in pathes:
            dirname: str = os.path.join(s.TXT_DIR, title)
            filename = re.match(r"^.*/(.*)\.\w+$", path)[1] + ".txt"
            to_path = os.path.join(dirname, filename)
            vtt2txt.parse_subtitles(from_path=path, to_path=to_path)

    elif service == s.SERVICE_NETFLIX:
        # Download Subtitles
        dirname: str = os.path.join(s.XML_DIR, title)
        urls: list = http.get_urls(url, service)
        pathes: list = http.download_all_subtitles(urls, dirname, service)

        # Parse Subtitles
        for path in pathes:
            dirname: str = os.path.join(s.TXT_DIR, title)
            filename = s.DEFAULT_TXT_FILENAME
            to_path = os.path.join(dirname, filename)
            xml2txt.parse_subtitles(from_path=path, to_path=to_path)


# DisneyPlus: vtt
# url: str = "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils/http/vtt/seg_00000.vtt"
# title: str = "test"
# service: str = s.SERVICE_DISNEYPLUS

# Netflix: xml
url: str = "https://ipv4-c004-itm001-k-opticom-isp.1.oca.nflxvideo.net/?o=1&v=99&e=1684854721&t=hq4U4_pN9ylDfuCYJaAd5tIrm8W7qHvICyGM6kNfx-zoYXdeNCK_PmqxE5QiPbueJEJ2p9gLJMz3EMTyUs6QjzdJqJfBQvgXh6gQDEfVH_11hdqSPS-GDG3htzs1kuKsdxlVsJ6HXa_jTQNQCdSyAOUN5j7xeQQ0r3fbi8SlyWMWeufOoDyUQ_OFb_RZLLZVYSqqs3O_sZ-PaymJikpiuK0cmVq-9W5DTYGKXNBFWcoEXg"
title: str = "kid_cosmic"
service: str = s.SERVICE_NETFLIX

main(url, title, service)
