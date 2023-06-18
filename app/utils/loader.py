import re

from app.models import Episode, Line
from app.utils import filter, parser_vtt, parser_xml


def load_subs(path: str, title: str):
    entries = []
    episode = Episode.objects.get_or_create(title=title)
    extension = re.match(r".*\.(\w+)$", path)[1]  # Ex. vtt, xml

    if extension == "vtt":
        lines = parser_vtt.parse_vtt(path)

    elif extension == "xml":
        lines = parser_xml.parse_xml(path)

    lines = filter.merge(lines)
    line_count = Line.objects.filter(episode__title=title).count()

    for i, line in enumerate(lines, line_count + 1):
        timestamp, text = line
        entries.append(
            Line(episode=episode[0], timestamp=timestamp, text=text, line_number=i)
        )

    return Line.objects.bulk_create(entries)


def reload_subs(path: str, title: str):
    Episode.objects.filter(title=title).delete()
    return load_subs(path, title)
