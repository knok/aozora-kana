# -*- coding: utf-8 -*-
#

import re
from enum import Enum

class ReadState(Enum):
    HEADER = 1
    NOTICE = 2
    BODY = 3
    FOOTER = 4

def remove_headfoot(file):
    # 予想する形式:
    # title, author
    # ---- (delimiter)
    # notice
    # ---- (delimiter)
    # body
    # 底本: name
    state = ReadState.HEADER
    ret = []
    for _line in file:
        line = _line.decode('cp932', "ignore")
        if line.startswith("--------"):
            if state == ReadState.HEADER:
                state = ReadState.NOTICE
            elif state == ReadState.NOTICE:
                state = ReadState.BODY
            elif state == ReadState.BODY:
                continue # just ignore
            else:
                raise ValueError("state: %s" % str(state))
            continue
        if line.startswith("底本：") and state == ReadState.BODY:
            state = ReadState.FOOTER
            continue
        if state == ReadState.BODY:
            ret.append(line)
    return ret

def remove_ruby(line):
    text = re.sub(r'｜([^《]+)《[^《]+》', r'\1', line)
    text = re.sub(r'《[^《]+》', '', text)
    return text

def remove_notice(line):
    text = re.sub(r'［＃.+］', '', line)
    return text

def remove_spaces(line):
    text = re.sub(r'\s+', '', line)
    return text

def process_sjis_rtext(file):
    lines = remove_headfoot(file)
    ret = []
    for line in lines:
        _line = remove_ruby(line)
        _line = remove_notice(_line)
        _line = remove_spaces(_line)
        if _line == "":
            continue
        ret.append(_line)
    return ret
