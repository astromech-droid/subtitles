from utils import files, parsers


def parse_lines(lines: list) -> list:
    lines = parsers.remove_linenumbers(lines)
    lines = parsers.remove_headers(lines)
    lines = parsers.remove_blanklines(lines)
    lines = parsers.extruct_starttime(lines)
    lines = parsers.put_starttime_on_alllines(lines)
    lines = parsers.merge_multilines(lines)
    return lines


def parse_subtitles(from_path: str, to_path: str) -> bool:
    lines: list = files.get_lines(from_path)
    lines = parse_lines(lines)

    result: bool = files.save_lines(lines, to_path)
    return result
