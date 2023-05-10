import os
from enum import Enum

OUT_DIR = "vtt"
TXT_DIR = "txt"
TEST_DIR = "tests"
TEST_DATA_DIR = os.path.join(TEST_DIR, "data")
MAX_SEGMENTS = 75  # 3h = 360min, 5min/vtt, 360/5 = 75vtt


class Service(Enum):
    DISNEYPLUS = "disneyplus"
