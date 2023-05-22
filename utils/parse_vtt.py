import os

import settings as s

from utils import parsers


def _parse(lines: list) -> list:
    lines = parsers.remove_linenumbers(lines)
    lines = parsers.remove_headers(lines)
    lines = parsers.remove_headers(lines)
    lines = parsers.remove_blanklines(lines)
    lines = parsers.extruct_starttime(lines)
    lines = parsers.put_starttime_on_alllines(lines)
    lines = parsers.merge_multilines(lines)

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
                lines = _parse(f_input.readlines())

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
            lines = parsers(f_input.readlines())

        with open(out_path, "w") as f_output:
            f_output.writelines(lines)
