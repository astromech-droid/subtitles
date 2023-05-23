from subtitles import subtitles

url = "https://sample.com/test.vtt"
title = "disneyplus_s1e1"

pathes = subtitles.run(url, title)

for path in pathes:
    print(path)
