This webapp was developed using Flask and is suitable to be easily deployed as a Google App Engine standard environment application.

With `gcloud` setup on local and provided there is one project which have AppEngine enabled, this directory containing the source can be deployed to the web, via: `gcloud app deploy` command.

For web preview of the currently deployed app, please use: https://code-search-dot-code-crafts-1477836554331.el.r.appspot.com/

For running the webapp locally (will run at `http://localhost:5000/`), please use the following:

```
pip install -r requirements.txt
export PORT=5000
gunicorn --bind :$PORT --workers 1 05-server:app 
```

<hr>

**Alert**: If you're willing to review the source code for this project and have reached this directory in pursuit of code review, please consider reviewing in the following sequence:

1. [01-data-ops-preprocessing.ipynb](./01-data-ops-preprocessing.ipynb)
2. [02-data-ops-classification-experiment.ipynb](./02-data-ops-classification-experiment.ipynb)
3. [03-data-ops-classification-final.ipynb](./03-data-ops-classification-final.ipynb)
4. [04-create_ir_idx.py](./04-create_ir_idx.py)
5. [05-server.py](./05-server.py)

For more details about the implementation and description of respective `*.py` and `*.ipynb` files, please refer to the [project documentation](../DOCUMENTATION.md).
