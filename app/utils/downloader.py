import os
import re
import time

import requests
from app.utils import settings


def download_subs(url: str, path: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        with open(path, "w") as f:
            f.write(response.text)

        return path

    else:
        return ""


def download_segments(url: str, dirname: str) -> list[str]:
    pathes = []

    for i in range(settings.UTILS_MAX_SEGMENTS):
        filename = f"seg_{str(i).zfill(5)}.vtt"
        _url = re.match(r"^(.*/)seg_\d{5}.vtt", url)[1] + filename
        path = download_subs(_url, os.path.join(dirname, filename))

        if path == "":
            break
        else:
            pathes.append(path)
            time.sleep(settings.UTILS_DOWNLOAD_SEGMENTS_INTERVAL)

    return pathes
