import settings as s
from lib.download_vtt import download

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
