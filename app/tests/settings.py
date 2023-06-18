TEST_TMP_DIR = "app/tests/tmp"

TEST_XML_PATH = "app/tests/data/test.xml"
TEST_XML_VALUE = [
    ("00:13:25.000", "-Leave town for adventure. -[both] What did you say?"),
    ("00:10:21.454", "But we've been here for all time, since I was born!"),
    ("00:01:45.063", "You can handle a few minutes up here."),
    ("00:05:32.000", "I don't want him"),
    ("00:05:32.000", "dicking you around tonight."),
    ("00:02:15.292", "I live at 308 Negra Arroyo Lane,"),
    ("00:02:18.250", "Albuquerque, New Mexico, 87104."),
    ("01:00:08.980", "Appreciate it."),
]

TEST_VTT_PATH = "app/tests/data/test.vtt"
TEST_VTT_VALUE = [
    ("00:00:09.083", "(THEME MUSIC PLAYING)"),
    ("00:00:31.750", "BONNIE: <i>We're real proud of you, Judy.</i>"),
    ("00:00:33.333", "STU: Yeah, scared too. BONNIE: Yes."),
    ("00:34:36.120", "Timeliness means something in"),
    ("00:34:38.000", "the world of theater, young lady."),
    ("00:18:55.520", "After all,"),
    ("00:18:57.880", "she loves pi."),
]
TEST_VTT_URL = "https://raw.githubusercontent.com/astromech-droid/subtitles/main/app/tests/data/test.vtt"

TEST_FILTER_VALUE = {
    "before": [
        ("00:00:33.333", "STU: Yeah, scared too. BONNIE: Yes."),
        ("00:18:55.520", "After all,"),
        ("00:18:57.880", "she loves pi."),
    ],
    "after": [
        ("00:00:33.333", "STU: Yeah, scared too. BONNIE: Yes."),
        ("00:18:55.520", "After all, she loves pi."),
    ],
}
