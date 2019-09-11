# -*- coding: utf-8 -*-

import zipfile
import os
import re
from enum import Enum

import sys
sys.path.append(
    os.path.join(os.path.dirname(
        os.path.abspath(__file__)
    ), "../")
)
from utils import remove_headfoot, process_sjis_rtext

def zip_files(basedir):
    files = []
    for fname in os.listdir(basedir):
        if not fname.endswith(".zip"):
            continue
        files.append("%s/%s" % (basedir, fname))
    return files

def read_zip_text(zip_fname):
    with zipfile.ZipFile(zip_fname) as f:
        fi = f.filelist[0]
        with f.open(fi.filename, 'r') as r:
            lines = process_sjis_rtext(r)
    return fi.filename, lines

def main():
    basedir = "zip/new"
    files = zip_files(basedir)
    fname, lines = read_zip_text(files[0])
    print(lines)

if __name__ == "__main__":
    main()
