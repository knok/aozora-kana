#
# usage: https://github.com/google/sentencepiece/blob/master/python/README.md

#%%
import sentencepiece as spm

#%%
fname = "plain/all.txt"
modelname = "tokenize/spm.model"

#%%
sp = spm.SentencePieceProcessor()
sp.Load(modelname)

#%%
with open(fname) as f:
    line = next(f)
    print(sp.EncodeAsPieces(line))
    print(sp.EncodeAsIds(line))

#%%
