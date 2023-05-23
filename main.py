from subtitles.conf import settings as s
from subtitles.core import vtt2txt, xml2txt


def main(url: str, title: str, service: str):
    if service == s.SERVICE_DISNEYPLUS:
        pathes = vtt2txt.run(url, title, service)

    elif service == s.SERVICE_NETFLIX:
        pathes = xml2txt.run(url, title, service)

    return pathes


# DisneyPlus: vtt
url: str = "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils/http/vtt/seg_00000.vtt"
title: str = "disneyplus_s1e1"
service: str = s.SERVICE_DISNEYPLUS

pathes = main(url, title, service)

for path in pathes:
    print(path)


# Netflix: xml
url: str = "https://ipv4-c004-itm001-k-opticom-isp.1.oca.nflxvideo.net/?o=1&v=99&e=1684854721&t=hq4U4_pN9ylDfuCYJaAd5tIrm8W7qHvICyGM6kNfx-zoYXdeNCK_PmqxE5QiPbueJEJ2p9gLJMz3EMTyUs6QjzdJqJfBQvgXh6gQDEfVH_11hdqSPS-GDG3htzs1kuKsdxlVsJ6HXa_jTQNQCdSyAOUN5j7xeQQ0r3fbi8SlyWMWeufOoDyUQ_OFb_RZLLZVYSqqs3O_sZ-PaymJikpiuK0cmVq-9W5DTYGKXNBFWcoEXg"
title: str = "netflix_s1e1"
service: str = s.SERVICE_NETFLIX
main(url, title, service)

pathes = main(url, title, service)
for path in pathes:
    print(path)
