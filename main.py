import os
import re

import settings as s
from core import vtt
from utils import http


def main(url: str, title: str, service: str):
    # Download Subtitles
    dirname: str = os.path.join(s.VTT_DIR, title)
    urls: list = http.get_urls(url, service)
    pathes: list = http.download_all_subtitles(urls, dirname)

    # Parse Subtitles
    for path in pathes:
        dirname: str = os.path.join(s.TXT_DIR, title)
        filename = re.match(r"^.*/(.*)\.\w+$", path)[1] + ".txt"
        to_path = os.path.join(dirname, filename)
        vtt.parse_subtitles(from_path=path, to_path=to_path)

    # vtt.parse_subtitles()


url: str = "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils/http/vtt/seg_00000.vtt"
title: str = "test"
service: str = s.SERVICE_DISNEYPLUS

main(url, title, service)


# import settings as s
# from utils.http import download
# from utils.parse_vtt import parse_and_save as vtt_parse_and_save
# from utils.parse_xml import parse_and_save as xml_parse_and_save

# For DisneyPlus
# url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/cca28bc2-eb49-476a-af99-173d06cfafc8/r/bf6f3bfc-01e1-4270-b605-264de963aab0/3737-MAIN/06/subtitles_1/seg_00001.vtt"
# dirname = "zootopia_plus_s1e2"
# url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/94dda514-70f4-4ebe-accd-457a2fa3b43b/r/4858c23f-b09d-4e38-89f7-143194a4414d/2e60-MAIN/06/subtitles_1/seg_00006.vtt"
# dirname = "monsters_inc"
# service = s.Service.DISNEYPLUS

# download(url, dirname, service)
# vtt_parse_and_save(dirname, service)

"""
# For Netflix (XML)
# dirname = "little_witch_academia_s2e14"
dirname = "romantic_killer_s1e2"
# dirname = "glitch_techs_s1e1"
# dirname = "kipo_s1e1"
# dirname = "hilda_s1e1"
# dirname = "the_mist_s1e1"
service = s.Service.NETFLIX
xml_parse_and_save(dirname, service)
"""

# For Netflix (VTT)
# dirname = "kid_cosmic"
# service = s.Service.NETFLIX
# vtt_parse_and_save(dirname, service)
