import copy
import os
import re

import settings as s


def remove_linenumbers(lines: list) -> list:
    new_lines = []

    for line in lines:
        if re.match(r"^\d+\n$", line):
            pass

        else:
            new_lines.append(line)

    return new_lines


def remove_headers(lines: list) -> list:
    for line in copy.copy(lines):
        starttime = re.match(r"(^\d{2}:\d{2}:\d{2}.\d{3}) -->.*", line)

        if starttime is None:
            lines.pop(0)

        else:
            break

    return lines


def remove_blanklines(lines: list) -> list:
    new_lines = []

    for line in lines:
        if not line == "\n":
            new_lines.append(line)

    return new_lines


def extruct_starttime(lines: list) -> list:
    new_lines = []

    for line in lines:
        starttime = re.match(r"(^\d{2}:\d{2}:\d{2}.\d{3}) -->.*", line)

        if starttime is None:
            new_lines.append(line)
        else:
            new_lines.append(starttime[1] + "\n")

    return new_lines


def put_starttime_on_alllines(lines: list) -> list:
    new_lines = []
    queue = []

    for line in lines:
        starttime = re.match(r"(^\d{2}:\d{2}:\d{2}.\d{3}).*", line)

        if starttime is None:
            new_lines.append(f"{queue[0]}: {line}")

        else:
            queue.clear()
            queue.append(starttime[1])

    return new_lines


def merge_multilines(lines: list) -> list:
    starttime_queue = []
    text_queue = []
    new_lines = []

    for line in lines:
        _line = re.match(r"(^\d{2}:\d{2}:\d{2}.\d{3}): (.*)\n", line)

        if _line is not None:
            starttime = _line[1]
            text = _line[2]

            text_queue.append(text)

            if len(starttime_queue) == 0:
                starttime_queue.append(starttime)

            if re.match(r"(.*\w$|.*,$)", text_queue[len(text_queue) - 1]) is None:
                new_lines.append(f"{starttime_queue[0]}: {str(' ').join(text_queue)}\n")
                starttime_queue.clear()
                text_queue.clear()

    return new_lines


def parse(lines: list) -> list:
    lines = remove_linenumbers(lines)
    lines = remove_headers(lines)
    lines = remove_headers(lines)
    lines = remove_blanklines(lines)
    lines = extruct_starttime(lines)
    lines = put_starttime_on_alllines(lines)
    lines = merge_multilines(lines)

    return lines


def parse_and_save(dirname, service):
    if service == s.Service.DISNEYPLUS:
        vtt_dir = os.path.join(s.OUT_DIR, dirname)
        txt_dir = os.path.join(s.TXT_DIR, dirname)

        vtt_filenames = os.listdir(vtt_dir)

        for vf in sorted(vtt_filenames):
            vtt_path = os.path.join(vtt_dir, vf)
            out_path = (
                vtt_path.replace("seg_", "parsed_")
                .replace(".vtt", ".txt")
                .replace(s.OUT_DIR, s.TXT_DIR)
            )

            if not os.path.exists(txt_dir):
                os.makedirs(txt_dir)

            with open(vtt_path, "r") as f_input:
                lines = parse(f_input.readlines())

            with open(out_path, "w") as f_output:
                f_output.writelines(lines)

    elif service == s.Service.NETFLIX:
        vtt_dir = os.path.join(s.OUT_DIR, dirname)
        txt_dir = os.path.join(s.TXT_DIR, dirname)

        vtt_path = os.path.join(vtt_dir, "subtitle.vtt")
        out_path = os.path.join(txt_dir, "subtitle.txt")

        if not os.path.exists(txt_dir):
            os.makedirs(txt_dir)

        # Netflix's vtt is encoded by UTF-8 with BOM.
        # So using "utf-8-sig"
        with open(vtt_path, "r", encoding="utf-8-sig") as f_input:
            lines = parse(f_input.readlines())

        with open(out_path, "w") as f_output:
            f_output.writelines(lines)
