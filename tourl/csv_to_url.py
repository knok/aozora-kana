# %%

import csv
import os
import random
import subprocess

fname = "./listinfo/list_person_all_extended_utf8.csv"


#%%
type_idx = 9
url_idx = 45
oldkana_list = []
newkana_list = []
with open(fname) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[type_idx] == "新字新仮名":
            newkana_list.append(row[url_idx])
        elif row[type_idx] == "新字旧仮名":
            oldkana_list.append(row[url_idx])

#%%

# aozora URL:
# https://www.aozora.gr.jp/cards/001265/files/46817_ruby_24669.zip
# github URL:
# https://github.com/aozorabunko/aozorabunko/raw/master/cards/000005/files/53194_ruby_44732.zip
#
def aozora2github(url):
    base_path = url[24:]
    ret = "https://github.com/aozorabunko/aozorabunko/raw/master" + \
        base_path
    return ret

#%%
len(oldkana_list), len(newkana_list)
# 4295, 10131
#%%
num_files = 4000 # treat 4000 files
dir_zip = "./zip"
dir_old = "./zip/old"
dir_new = "./zip/new"

def imkdir(d):
    if not os.path.exists(d):
        os.makedirs(d)
for d in [dir_zip, dir_old, dir_new]:
    imkdir(d)

curdir = os.getcwd()
os.chdir(dir_old)
random.shuffle(oldkana_list)
for i, url in enumerate(oldkana_list):
    if i > num_files:
        break
    gurl = aozora2github(url)
    subprocess.call(["wget", "-c", gurl])
os.chdir(curdir)
#%%
# curdir = os.getcwd()
os.chdir(dir_new)
random.shuffle(newkana_list)
for i, url in enumerate(newkana_list):
    if i > num_files:
        break
    gurl = aozora2github(url)
    subprocess.call(["wget", "-c", gurl])
