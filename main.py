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


def main():
    # url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/04cc23e7-6795-4239-afd8-b9ef95b6af9d/r/f914d404-8913-46c3-8db7-c1422f2baa13/d678-MAIN/06/subtitles_1/seg_00000.vtt"
    # dirname = "modern_family_s7e9"
    # url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/03afb8b7-08ad-4bf6-852c-9009d2d2707b/r/0425e9c9-4650-4a6e-b1b7-a295093ee532/3769-MAIN/06/subtitles_1/seg_00000.vtt"
    # dirname = "modern_family_s7e10"
    # url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/b8fc3a24-ca32-4879-97f7-befffaa7003c/r/9d54313d-40a8-4327-accd-88e6ba0d3a87/af0a-MAIN/06/subtitles_1/seg_00000.vtt"
    # dirname = "modern_family_s7e11"
    url = "https://vod-akc-ap-north-1.media.dssott.com/ps01/disney/9d81e6fe-6f53-40da-a620-b66e720a47be/r/d5f4cde3-14e1-47bf-8bad-035f15e844f4/b378-MAIN/06/subtitles_1/seg_00000.vtt"
    dirname = "modern_family_s7e12"
    service = s.Service.DISNEYPLUS

    download(url, dirname, service)


main()
