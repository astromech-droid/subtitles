import os
import re
import time

import requests
import settings as s

from utils import files


def _fetch_text(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return ""


def get_urls(url: str, service: str) -> list:
    urls = []

    if service == s.SERVICE_DISNEYPLUS:
        for i in range(0, s.MAX_SEGMENTS):
            url_head = re.match(r"(^https://.*/)seg_\d{5}.vtt", url)[1]
            seg_filename = f"seg_{str(i).zfill(5)}.vtt"
            urls.append(f"{url_head}{seg_filename}")

    elif service == s.SERVICE_NETFLIX:
        urls.append(url)

    else:
        pass

    return urls


def download_subtitles(url: list, path: str) -> bool:
    text: str = _fetch_text(url)
    result: bool = files.save_text(text, path)
    return result


def download_all_subtitles(urls: list, dirname: str) -> list:
    for url in urls:
        filename: str = re.match(r"^https://.*/(.*)", url)[1]
        path: str = os.path.join(dirname, filename)
        result: bool = download_subtitles(url, path)

        if result is False:
            break

        time.sleep(1)

    return os.listdir(dirname)
