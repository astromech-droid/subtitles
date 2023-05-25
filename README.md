# Usage
##### Download
```python
from subtitles.conf import settings
from subtitles.subtitles import Subtitles

service: str = settings.SERVICE_NETFLIX
title: str = "breaking_bad_s1e1"
subtitles = Subtitles(service, title)

url = "https://url/to/subtitles"
subtitles.download(url)

print(f"download to {subtitles.downloader.dirname}")
```
##### Read
```python
path = "path/to/a/file"
lines = subtitles.read(path)

for starttime, text in lines:
    print(f"{starttime}: {text}")
    # 00:00:13.334: [♪♪♪]
    # 00:00:28.209: [PANTING]
    # 00:00:29.459: [GLASS SHATTERING]
    # 00:01:00.667: [GRUNTING]
    # 00:01:07.584: Oh, my God. Christ!
    # 00:01:14.834: Shit.
```
##### Write
```
path = "path/to/a/file"
lines = subtitles.read("path/to/a/src/file")

subtitles.write(path, lines)
```
# Tips
#### How to get url of subtitles from Netflix
* Login to netflix
* Open developer tools
* Open network tab
* Start the video
* Pause the video
* Press clear and input "/?o="" as filter
* Choose a subtitle