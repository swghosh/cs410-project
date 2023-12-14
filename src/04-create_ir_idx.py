import pandas as pd
import os
import metapy

df = pd.read_json('./data/dataset.json')

# sanitize \n and \r in doc strings
docs = []
for idx, row in df.iterrows():
    d = ''
    try:
        xn = row['content'].split('\n')
        d = ' \\n '.join(xn)
    except:
        pass
    try:
        xr = d.split('\r')
        d = ' \\r '.join(xr)
    except:
        pass
    docs.append(d)

os.makedirs("./data/dataset", exist_ok=True)

# write .dat file
with open('./data/dataset/dataset.dat', 'w') as f:
    for doc in docs:
        print(doc, file=f, end='\n')

# write config toml(s)
with open('./data/dataset/line.toml', 'w') as f:
    print('type = "line-corpus"', file=f, end='\n')

with open('./meta-config.toml', 'w') as f:
    print("""
prefix = "./data"

dataset = "dataset"
corpus = "line.toml"
index = "idx"

[[analyzers]]
method = "ngram-word"
ngram = 1
filter = [{type = "icu-tokenizer"}, {type = "lowercase"}]
""", file=f, end='\n')

# create the inverted index (will save to disk)
idx = metapy.index.make_inverted_index('meta-config.toml')
