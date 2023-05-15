import settings as s
from lib.download_vtt import download
from lib.parse_vtt import parse_and_save as vtt_parse_and_save
from lib.parse_xml import parse_and_save as xml_parse_and_save

"""
# For DisneyPlus
url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/cca28bc2-eb49-476a-af99-173d06cfafc8/r/bf6f3bfc-01e1-4270-b605-264de963aab0/3737-MAIN/06/subtitles_1/seg_00001.vtt"
dirname = "zootopia_plus_s1e2"
service = s.Service.DISNEYPLUS

download(url, dirname, service)
vtt_parse_and_save(dirname, service)
"""

# For Netflix
# dirname = "little_witch_academia_s2e14"
# dirname = "romantic_killer_s1e1"
# dirname = "glitch_techs_s1e1"
dirname = "kipo_s1e1"
service = s.Service.NETFLIX

xml_parse_and_save(dirname, service)
