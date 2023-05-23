import os

OUTPUT_DIR = "output"
VTT_DIR = os.path.join(OUTPUT_DIR, "vtt")
XML_DIR = os.path.join(OUTPUT_DIR, "xml")
TXT_DIR = os.path.join(OUTPUT_DIR, "txt")

TEST_DIR = "tests"
TEST_DATA_DIR = os.path.join(TEST_DIR, "data")

SERVICE_DISNEYPLUS = "disneyplus"
SERVICE_NETFLIX = "netflix"

MAX_SEGMENTS = 75  # 3h = 360min, 5min/vtt, 360/5 = 75vtt

DEFAULT_TXT_FILENAME = "subtitle.txt"
DEFAULT_XML_FILENAME = "subtitle.xml"
