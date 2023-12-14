from flask import Flask, render_template, request
from functools import cmp_to_key

import pandas as pd
import json
import metapy
import joblib
import numpy as np

data_df = pd.read_json("./data/dataset.json")

idx = metapy.index.make_inverted_index('meta-config.toml')
ranker = metapy.index.OkapiBM25()

model = joblib.load('./data/model.joblib')
cats = {
    0: 'Linux (Ubuntu, RHEL, Fedora, Debian, CentOS etc.)', 
    1: 'Windows',
}

app = Flask(__name__)
icons_b64 = json.load(open('./data/icons.json'))


def search_query(query):
    doc = metapy.index.Document()
    doc.content(query)
    top_docs = ranker.score(idx, doc, num_results=6)
    doc_ids = [t[0] for t in top_docs]
    
    top_items = [data_df.loc[i] for i in doc_ids]
    top_items = [
        {
            "repo": item["sample_repo_name"],
            "path": item["sample_path"],
            "content": item["original_content"] if item["original_content"] else item["content"],
            "icon": icons_b64[item["source_category"]]
        } for item in top_items
    ]
    top_items = sorted(top_items, key=cmp_to_key(lambda s1, s2: - (len(s1["content"].split('\n')) - len(s2["content"].split('\n')))))
    return top_items

def classify_query(query):
    predicted_probas = model.predict_proba(np.array(query)[None])[0]

    results = [
        {"category": cats[i], "percentage": float(proba)} for i, proba in enumerate(predicted_probas)
    ]
    results = sorted(results, key=cmp_to_key(lambda x1, x2: - (x1["percentage"] - x2["percentage"])))
    return results

def search_and_classify(query):
    results = classify_query(query)
    top_items = search_query(query)
    return results, top_items

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results, top_items = search_and_classify(query)
        return render_template('results.html', results=results, top_items=top_items, query=query)
    else:
        query = request.args.get("query")
        query = "" if query is None else query
        return render_template('index.html', query=query)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
