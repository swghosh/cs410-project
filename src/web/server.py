from flask import Flask, render_template, request
import random  
from functools import cmp_to_key

import pandas as pd
import pdb

data_df = pd.read_json("./data/dataset.json")

app = Flask(__name__)

def search_database(query):
    # Placeholder for database query, replace this with your implementation
    # For now, generate dummy data
    results = [
        {"category": "RHEL, Fedora, Rocky, CentOS etc.", "percentage": random.uniform(0, 100)},
        {"category": "Ubuntu, Debian etc. ", "percentage": random.uniform(0, 100)},
        {"category": "Windows", "percentage": random.uniform(0, 100)},
        {"category": "Unknown or others", "percentage": random.uniform(0, 100)},
    ]
    percent_sum = sum([i["percentage"] for i in results])
    for result in results:
        result["percentage"] = result["percentage"] / percent_sum

    results = sorted(results, key=cmp_to_key(lambda x1, x2: - (x1["percentage"] - x2["percentage"])))

    top_items = [
        data_df.loc[random.randint(0, len(data_df) - 1)],
        data_df.loc[random.randint(0, len(data_df) - 1)],
        data_df.loc[random.randint(0, len(data_df) - 1)],
        data_df.loc[random.randint(0, len(data_df) - 1)],
        data_df.loc[random.randint(0, len(data_df) - 1)],
        data_df.loc[random.randint(0, len(data_df) - 1)],
    ]
    top_items = [
        {
            "repo": item["sample_repo_name"],
            "path": item["sample_path"],
            "content": item["original_content"] if item["original_content"] else item["content"]
        } for item in top_items
    ]
    top_items = sorted(top_items, key=cmp_to_key(lambda s1, s2: - (len(s1["content"].split('\n')) - len(s2["content"].split('\n')))))
    return results, top_items

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results, top_items = search_database(query)
        return render_template('results.html', results=results, top_items=top_items, query=query)
    else:
        query = request.args.get("query")
        query = "" if query is None else query
        return render_template('index.html', query=query)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
