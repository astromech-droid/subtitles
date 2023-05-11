import settings as s
from lib.download_vtt import download
from lib.parse_vtt import parse_and_save as vtt_parse_and_save
from lib.parse_xml import parse_and_save as xml_parse_and_save

"""
# For DisneyPlus
url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/3381ebdf-7449-47dc-aaa9-b8040163a09e/r/b8c23d40-7d49-4998-bc65-aa4160d3622a/13dd-MAIN/06/subtitles_1/seg_00000.vtt"
dirname = "modern_family_s7e13"
service = s.Service.DISNEYPLUS

download(url, dirname, service)
vtt_parse_and_save(dirname, service)
"""

# For Netflix
dirname = "little_witch_academia_s2e14"
service = s.Service.NETFLIX

xml_parse_and_save(dirname, service)
