TEST_TMP_DIR = "app/tests/tmp"

TEST_XML_PATH = "app/tests/data/test.xml"
TEST_XML_VALUE = [
    ("00:13:25.000", "-Leave town for adventure."),
    ("00:13:25.000", "-[both] What did you say?"),
    ("00:10:21.454", "But we've been here for all time,"),
    ("00:10:21.454", "since I was born!"),
    ("00:01:45.063", "You can handle a few minutes up here."),
    ("00:05:32.000", "I don't want him"),
    ("00:05:32.000", "dicking you around tonight."),
    ("00:02:15.292", "I live at 308 Negra Arroyo Lane,"),
    ("00:02:18.250", "Albuquerque, New Mexico, 87104."),
    ("01:00:08.980", "Appreciate it."),
    ("00:41:15.473", "[Phil] Come in, Mitch."),
    ("00:01:10.821", "-[meowing]"),
    ("00:01:10.821", "-But the love of my life is Momohiki!"),
    ("00:18:37.408", "[Anzu] So far, the sleeping arrangements have been kinda nice."),
]
TEST_XML_FILTERED_VALUE = [
    ("00:13:25.000", "-Leave town for adventure."),
    ("00:13:25.000", "-[both] What did you say?"),
    ("00:10:21.454", "But we've been here for all time, since I was born!"),
    ("00:01:45.063", "You can handle a few minutes up here."),
    ("00:05:32.000", "I don't want him dicking you around tonight."),
    ("00:02:15.292", "I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104."),
    ("01:00:08.980", "Appreciate it."),
    ("00:41:15.473", "[Phil] Come in, Mitch."),
    ("00:01:10.821", "-[meowing]"),
    ("00:01:10.821", "-But the love of my life is Momohiki!"),
    ("00:18:37.408", "[Anzu] So far, the sleeping arrangements have been kinda nice."),
]

TEST_VTT_PATH = "app/tests/data/test.vtt"
TEST_VTT_VALUE = [
    ("00:17:42.270", "but it still feels kind of warped to me."),
    ("00:00:09.083", "(THEME MUSIC PLAYING)"),
    ("00:00:31.750", "BONNIE: <i>We're real proud of you, Judy.</i>"),
    ("00:00:33.333", "STU: Yeah, scared too."),
    ("00:00:33.333", "BONNIE: Yes."),
    ("00:34:36.120", "Timeliness means something in"),
    ("00:34:38.000", "the world of theater,"),
    ("00:34:38.000", "young lady."),
    ("00:18:55.520", "After all,"),
    ("00:18:57.880", "she loves pi."),
    ("00:03:10.457", "<i>Simulation terminated.</i>"),
    ("00:03:10.457", "<i>Simulation terminated.</i>"),
    ("01:08:39.875", "Wait a minute. You turned on the TV"),
    ("01:08:39.875", "last night, not Jessie."),
    ("00:17:40.185", "And they're nice enough to feed us,"),
]
TEST_VTT_FILTERED_VALUE = [
    ("00:17:42.270", "but it still feels kind of warped to me."),
    ("00:00:09.083", "(THEME MUSIC PLAYING)"),
    ("00:00:31.750", "BONNIE: We're real proud of you, Judy."),
    ("00:00:33.333", "STU: Yeah, scared too."),
    ("00:00:33.333", "BONNIE: Yes."),
    ("00:34:36.120", "Timeliness means something in the world of theater, young lady."),
    ("00:18:55.520", "After all, she loves pi."),
    ("00:03:10.457", "Simulation terminated."),
    ("00:03:10.457", "Simulation terminated."),
    ("01:08:39.875", "Wait a minute. You turned on the TV last night, not Jessie."),
    ("00:17:40.185", "And they're nice enough to feed us,"),
]
TEST_VTT_URL = "https://raw.githubusercontent.com/astromech-droid/subtitles/main/app/tests/data/test.vtt"  # noqa: E501

TEST_SEGMENT_URLS = [
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/app/tests/data/segments/seg_00000.vtt",  # noqa: E501
    "https://raw.githubusercontent.com/astromech-droid/subtitles/main/app/tests/data/segments/seg_00001.vtt",  # noqa: E501
]
TEST_SEGMENT_PATHES = [
    "app/tests/data/segments/seg_00000.vtt",
    "app/tests/data/segments/seg_00001.vtt",
]

TEST_VTT_EPISODE_TITLE = "test_vtt_s1e1"
TEST_XML_EPISODE_TITLE = "test_xml_s1e1"

TEST_EPISODE_API_URL = f"http://localhost:8000/app/api/episodes/{TEST_VTT_EPISODE_TITLE}/"

TEST_WORDGUESSER_IGNORED = [
    ("00:00:09.083", "(THEME MUSIC PLAYING)"),
    ("00:00:09.083", "[THEME MUSIC PLAYING]"),
]
