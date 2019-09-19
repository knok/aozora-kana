# -*- coding: utf-8 -*-
#

#%%
import re
import os

#%%
srcdir = "plain/new"
outdir = "fold/new"
os.makedirs(outdir, exist_ok=True)

#%%
def text_files(basedir):
    files = []
    for fname in os.listdir(basedir):
        if not fname.endswith(".txt"):
            continue
        files.append("%s/%s" % (basedir, fname))
    return files


#%%
fs = text_files(srcdir)
fname = fs[0]

#%%

# 分割ルール
# * 長い行は「。」で分割
# * セリフである「」は基本分割しない
#   * "「"で始まったらセリフと判断
#   * セリフの"。」"が行末の印
#

#%%
def split_text(fd, max_len=150):
    ret = []
    for line in fd:
        line = line[:-1]
        if line.startswith("「"):
            ret.append(line)
            continue
        else:
            if len(line) < max_len:
                ret.append(line)
                continue
        # 長文の分割
        lines = re.split(r'。', line)
        lines = [l + "。" for l in lines]
        if lines[-1] == "。":
            lines.remove("。")
        ret.extend(lines)
    return ret


#%%
for fname in fs:
    out_fname = os.path.join(outdir, os.path.basename(fname))
    with open(fname) as f:
        lines = split_text(f)
    with open(out_fname, "w") as f:
        for line in lines:
            f.write(line)
            f.write('\n')

#%%
