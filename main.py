from subtitles.core.Subtitles import Subtitles

url = "https://sample.com/test.vtt"
title = "disneyplus_s1e1"

subtitles = Subtitles()
pathes = subtitles.run(url, title)

for path in pathes:
    print(path)
