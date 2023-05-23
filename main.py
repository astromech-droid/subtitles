import os
import re

from subtitles.conf import settings as s
from subtitles.core import vtt2txt, xml2txt
from subtitles.utils import http


def main(url: str, title: str, service: str):
    if service == s.SERVICE_DISNEYPLUS:
        dir: str = s.VTT_DIR

    elif service == s.SERVICE_NETFLIX:
        dir: str = s.XML_DIR

    # Download Subtitles
    dirname: str = os.path.join(dir, title)
    urls: list = http.get_urls(url, service)
    pathes: list = http.download_all_subtitles(urls, dirname, service)

    # Parse Subtitles
    for path in pathes:
        dirname_txt: str = os.path.join(s.TXT_DIR, title)

        if service == s.SERVICE_DISNEYPLUS:
            filename = re.match(r"^.*/(.*)\.\w+$", path)[1] + ".txt"
            to_path: str = os.path.join(dirname_txt, filename)
            vtt2txt.parse_subtitles(from_path=path, to_path=to_path)

        if service == s.SERVICE_NETFLIX:
            filename = s.DEFAULT_TXT_FILENAME
            to_path: str = os.path.join(dirname_txt, filename)
            xml2txt.parse_subtitles(from_path=path, to_path=to_path)


# DisneyPlus: vtt
url: str = "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils/http/vtt/seg_00000.vtt"
title: str = "disneyplus_s1e1"
service: str = s.SERVICE_DISNEYPLUS
main(url, title, service)

# Netflix: xml
url: str = "https://ipv4-c004-itm001-k-opticom-isp.1.oca.nflxvideo.net/?o=1&v=99&e=1684854721&t=hq4U4_pN9ylDfuCYJaAd5tIrm8W7qHvICyGM6kNfx-zoYXdeNCK_PmqxE5QiPbueJEJ2p9gLJMz3EMTyUs6QjzdJqJfBQvgXh6gQDEfVH_11hdqSPS-GDG3htzs1kuKsdxlVsJ6HXa_jTQNQCdSyAOUN5j7xeQQ0r3fbi8SlyWMWeufOoDyUQ_OFb_RZLLZVYSqqs3O_sZ-PaymJikpiuK0cmVq-9W5DTYGKXNBFWcoEXg"
title: str = "netflix_s1e1"
service: str = s.SERVICE_NETFLIX
main(url, title, service)
