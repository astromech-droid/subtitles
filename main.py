from subtitles.conf import settings
from subtitles.core.Subtitles import Subtitles

subtitles = Subtitles()

# DisneyPlus: vtt
url: str = settings.TEST_VTT_URL
title: str = "disneyplus_s1e1"

pathes = subtitles.run(url, title)
for path in pathes:
    print(path)


# Netflix: xml
url: str = settings.TEST_XML_URL
title: str = "netflix_s1e1"

pathes = subtitles.run(url, title)
for path in pathes:
    print(path)
