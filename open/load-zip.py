# -*- coding: utf-8 -*-

#%%
import zipfile
import os
import re
from enum import Enum
from utils import remove_headfoot, process_rtext

#%%
files = []
basedir = "zip/new"
for fname in os.listdir(basedir):
    if not fname.endswith(".zip"):
        continue
    files.append("%s/%s" % (basedir, fname))

#%%
f = zipfile.ZipFile(files[0])

#%%
fi = f.filelist[0]

#%%
with f.open(fi.filename, 'r') as r:
    for line in r:
        print(line.decode('shift_jis'), end="")

#%%
with f.open(fi.filename, 'r') as r:
    lines = remove_headfoot(r)
    for line in lines:
        print(line, end="")


#%%
def remove_ruby(line):
    text = re.sub(r'｜([^《]+)《[^《]+》', '\1', line)
    text = re.sub(r'《[^《]+》', '', text)
    return text
#%%
with f.open(fi.filename, 'r') as r:
    lines = remove_headfoot(r)
    for line in lines:
        _line = remove_ruby(line)
        print(_line, end="")


#%%
def remove_notice(line):
    text = re.sub(r'［＃.+］', '', line)
    return text

def remove_spaces(line):
    text = re.sub(r'\s+', '', line)
    return text

#%%
with f.open(fi.filename, 'r') as r:
    lines = remove_headfoot(r)
    for line in lines:
        _line = remove_ruby(line)
        _line = remove_notice(_line)
        _line = remove_spaces(_line)
        if _line == "":
            continue
        print(_line)


#%%
with f.open(fi.filename, 'r') as r:
    lines = process_sjis_rtext(r)
    for i, line in enumerate(lines):
        print("%d: %s" % (i, line))

#%%
with f.open(fi.filename, 'r') as r, open("tmp.txt", "w") as w:
    lines = process_sjis_rtext(r)
    for i, line in enumerate(lines):
        w.write(line)
        w.write('\n')
        print("%d: %s" % (i, line))


#%%
