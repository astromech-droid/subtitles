from subtitles.conf import settings
from subtitles.subtitles import Subtitles

service: str = settings.SERVICE_DISNEYPLUS
title: str = "title"

subtitles = Subtitles(service, title)
dirname_src = subtitles.downloader.dirname
dirname_dst = subtitles.parser.dirname_dst

print(dirname_src)
print(dirname_dst)
