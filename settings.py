import os

VTT_DIR = "vtt"
XML_DIR = "xml"
TXT_DIR = "txt"
TEST_DIR = "tests"
TEST_DATA_DIR = os.path.join(TEST_DIR, "data")

SERVICE_DISNEYPLUS = "disneyplus"
SERVICE_NETFLIX = "netflix"

MAX_SEGMENTS = 75  # 3h = 360min, 5min/vtt, 360/5 = 75vtt

DEFAULT_FILENAME = "subtitle.txt"
