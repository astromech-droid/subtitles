import os

# DIRECTRIES
OUTPUT_DIR = "output"
VTT_DIR = os.path.join(OUTPUT_DIR, "vtt")
XML_DIR = os.path.join(OUTPUT_DIR, "xml")
TXT_DIR = os.path.join(OUTPUT_DIR, "txt")
TEST_DIR = "tests"
TEST_DATA_DIR = os.path.join(TEST_DIR, "data")

# FILENAMES
DEFAULT_TXT_FILENAME = "subtitles.txt"
DEFAULT_XML_FILENAME = "subtitles.xml"
DEFAULT_VTT_FILENAME = "subtitles.vtt"

# SERVICES
SERVICE_DISNEYPLUS = "disneyplus"
SERVICE_NETFLIX = "netflix"

# PARAMETERS
MAX_SEGMENTS = 75  # 3h = 360min, 5min/vtt, 360/5 = 75vtt
DOWNLOAD_INTERVAL = 0.5

# TESTS
TEST_TITLE = "test"
TEST_URL_DISNEYPLUS_00 = str(
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils"
    "/http/vtt/disneyplus/seg_00000.vtt"
)

TEST_URL_DISNEYPLUS_01 = str(
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils"
    "/http/vtt/disneyplus/seg_00001.vtt"
)

TEST_URL_NETFLIX = str(
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data/utils"
    "/http/xml/netflix/subtitles.xml"
)
