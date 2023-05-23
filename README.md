# Usage
```python
from subtitles.core.Subtitles import Subtitles

url = "https://sample.com/test.vtt"
title = "disneyplus_s1e1"

subtitles = Subtitles()
pathes = subtitles.run(url, title)

for path in pathes:
    print(path)
```

# Tips
#### How to download subtitles from Netflix
* Login to netflix
* Open developer tools
* Open network tab
* Start the video
* Pause the video
* Press clear and input "/?o="" as filter
* Choose a subtitle