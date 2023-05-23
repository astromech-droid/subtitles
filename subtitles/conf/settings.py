import os

OUTPUT_DIR = "output"
VTT_DIR = os.path.join(OUTPUT_DIR, "vtt")
XML_DIR = os.path.join(OUTPUT_DIR, "xml")
TXT_DIR = os.path.join(OUTPUT_DIR, "txt")

TEST_DIR = "tests"
TEST_DATA_DIR = os.path.join(TEST_DIR, "data")

TEST_VTT_URL = (
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests"
    "/data/utils/http/vtt/disneyplus/seg_00000.vtt"
)

TEST_XML_URL = (
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests"
    "/data/utils/http/xml/netflix/subtitles.xml"
)

SERVICE_DISNEYPLUS = "disneyplus"
SERVICE_NETFLIX = "netflix"

MAX_SEGMENTS = 75  # 3h = 360min, 5min/vtt, 360/5 = 75vtt

DEFAULT_TXT_FILENAME = "subtitles.txt"
DEFAULT_XML_FILENAME = "subtitles.xml"
