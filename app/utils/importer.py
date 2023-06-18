import re

from app.models import Episode, Line
from app.utils import filter, parser_vtt, parser_xml


def import_subs(path: str, title: str):
    entries = []
    episode = Episode.objects.get_or_create(title=title)
    extension = re.match(r".*\.(\w+)$", path)[1]  # Ex. vtt, xml

    if extension == "vtt":
        lines = parser_vtt.parse_vtt(path)

    elif extension == "xml":
        lines = parser_xml.parse_xml(path)

    lines = filter.merge(lines)

    for i, line in enumerate(lines, 1):
        timestamp, text = line
        entries.append(
            Line(episode=episode[0], timestamp=timestamp, text=text, line_number=i)
        )

    return Line.objects.bulk_create(entries)
