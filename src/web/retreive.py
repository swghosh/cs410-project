import metapy
import sys

idx = metapy.index.make_inverted_index('meta-config.toml')

ranker = metapy.index.OkapiBM25()
query = metapy.index.Document()
query.content(' '.join(sys.argv[1:]))

top_docs = ranker.score(idx, query, num_results=5)
print([i[0] for i in top_docs])
