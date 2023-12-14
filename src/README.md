This webapp was developed using Flask and is suitable to be easily deployed as a Google App Engine standard environment application.

With `gcloud` setup on local and provided there is one project which have AppEngine enabled, this directory containing the source can be deployed to the web, via: `gcloud app deploy` command.

For web preview of the currently deployed app, please use: https://code-search-dot-code-crafts-1477836554331.el.r.appspot.com/

For running the webapp locally (will run at `http://localhost:5000/`), please use the following:

```
pip install -r requirements.txt
export PORT=5000
gunicorn --bind :$PORT --workers 1 05-server:app 
```
