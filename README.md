# Usage
```python
from subtitles import subtitles

url = "https://sample.com/test.vtt"
title = "disneyplus_s1e1"

pathes = subtitles.run(url, title)

for path in pathes:
    print(path)
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