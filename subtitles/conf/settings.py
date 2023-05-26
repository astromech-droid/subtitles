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
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data"
    "/downloader/seg_00000.vtt"
)

TEST_URL_DISNEYPLUS_01 = str(
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data"
    "/downloader/seg_00001.vtt"
)

TEST_URL_NETFLIX = str(
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/tests/data"
    "/downloader/subtitles.xml"
)

TEST_LINES_XML: list[tuple[str]] = [
    ("00:13:25.000", "-Leave town for adventure. -[both] What did you say?"),
    ("00:10:21.454", "But we've been here for all time, since I was born!"),
    ("00:01:45.063", "You can handle a few minutes up here."),
    ("00:05:32.000", "I don't want him dicking you around tonight."),
    ("00:02:15.292", "I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104."),
]

TEST_LINES_VTT: list[tuple[str]] = [
    ("00:00:09.083", "(THEME MUSIC PLAYING)"),
    ("00:00:31.750", "BONNIE: <i>We're real proud of you, Judy.</i>"),
    ("00:00:33.333", "STU: Yeah, scared too. BONNIE: Yes."),
    (
        "00:34:36.120",
        "DARBUS: Timeliness means something in the world of theater, young lady.",
    ),
    ("00:18:55.520", "After all, she loves pi."),
]
