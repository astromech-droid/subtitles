import os
import re
import time

import requests
import settings as s


def fetch(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return None


def save(vtt_text: str, path: str) -> None:
    with open(path, "w") as f:
        f.write(vtt_text)


def download(url, dirname, service):
    out_dir = os.path.join(f"./{s.OUT_DIR}", dirname)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if service == s.Service.DISNEYPLUS:
        for i in range(0, s.MAX_SEGMENTS + 1):
            url_head = re.match(r"(^https://.*/)seg_\d{5}.vtt", url)[1]
            seg_filename = f"seg_{str(i).zfill(5)}.vtt"
            vtt_text = fetch(url=f"{url_head}{seg_filename}")

            if vtt_text is None:
                break

            else:
                out_path = os.path.join(out_dir, seg_filename)
                save(vtt_text, out_path)
                time.sleep(1)
