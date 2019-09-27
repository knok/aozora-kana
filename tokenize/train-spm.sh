#!/bin/sh
#

cat plain/new/* > plain/all.txt
cat plain/old/+ >> plain/all.txt

spm_train --input=plain/all.txt --model_prefix=tokenize/spm \
 --vocab_size=8000 --character_coverage=1.0
 