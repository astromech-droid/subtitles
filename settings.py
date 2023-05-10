from enum import Enum

OUT_DIR = "vtt"
MAX_SEGMENTS = 75  # 3h = 360min, 5min/vtt, 360/5 = 75vtt


class Service(Enum):
    DISNEYPLUS = "disneyplus"
