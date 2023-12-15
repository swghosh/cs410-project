# Project Documentation

Project Title: **CodeSearch: Infer OS from script commands and retrieve related scripts for user query**

Author: **Swarup Ghosh** (Net ID: **swarupg2**)

Course-work: **CS 410 (Text Information Systems) Project, University of Illinois Urbana-Champaign**

## Overview

The project is a Flask-based web application designed to determine the underlying operating system (Linux or Windows) based on user-input of shell scripts, commands, or package names. Also, based upon the user query it provides relevant scripts with it's corresponding GitHub links.

The project is accessible for use from: **https://code-search-dot-code-crafts-1477836554331.el.r.appspot.com/**

**Brief**: 
- Input: shell script command keywords or entire shell script or single line from a script
- Output:
    - Classification: Windows / Linux
    - Retrieval: Top 6 Scripts and their GitHub links

## High Level Architecture

TODO

## Technology Stack

The primary programming language use for developing the project is Python. However, aside of that SQL was used to generate the Big Query queries involved in data collection and basic HTML, CSS was used to develop the web user interface.

In a nutshell, the stack consists of:
- Google Big Query (SQL statements)
- Python 3.7
    - Gunicorn (web server for Python WSGI web apps)
    - Flask (web app framework)
    - MeTaPy (text retrieval and inverted index creation)
    - Scikit-Learn (training of machine learning classifier)
    - Pandas (for pre-processing of collected data)
    - Joblib (persistence of Python objects to disk)
- Google App Engine (deployment)

## Implementation
The project consists of several components:
1. Data Collection and Preprocessing
    - SQL queries were crafted as per statemens in [**bq_queries.sql**](./data/bq_queries.sql) which were input on the Google Big Query online interface to collect data in the form of CSVs.
        - 3 CSVs were collected:
            1. [sample_contents_bat.csv](./data/sample_contents_bat.csv): collected 1413 random `*.bat` files from GitHub
            2. [sample_contents_dockerfile.csv](./data/sample_contents_dockerfile.csv): collected 2204 random `Dockerfile`(s) from GitHub
            3. [sample_contents_sh.csv](./data/sample_contents_sh.csv): collected 15626 random `*.sh` files from GitHub
    - Jupyter Notebook used for Data Pre-processing: [**01-data-ops-preprocessing.ipynb**](./src/01-data-ops-preprocessing.ipynb)
        - Combines the data from all the 3 CSVs, pre-processes the content present in the `Dockerfile`(s) and converts the meaningful information in shell script like contents. The output of all the data combined together (totalling to 19243 entries) is stored to [dataset.json](./src/data/dataset.json) file which is serialized as a pandas DataFrame to be persisted for re-use in later steps. 
2. Classification
    - Notebook for initial classification experiment: [**02-data-ops-classification-experiment.ipynb**](./src/02-data-ops-classification-experiment.ipynb)
        - The initial intent was to use manually generated labels using gathered keywords for each OS category. The OS categories attempted to be classified were: `['rhel/fedora', 'ubuntu/debian', 'windows', 'others/unknown']` by score them using a Bag of Words based unigram token giving a reward for each keyword matched across corresponding labels. However, this experiment did not go well and results were completely biased towards the `'others/unknown'` class which wasn't useful for the downstream task. The root cause for the problem was analyzed that the gathered keywords weren't effective/sufficient enough to reward and do automatic labelling of the large dataset of 19k documents irrespective of using different classifiers like SVM, Naive Bayes, etc. Hence, this approach was discarded but the proof-of-concept exists in the notebook. 
    - Notebook for final classification and model classification pipeline persistence: [**03-data-ops-classification-final.ipynb**](./src/03-data-ops-classification-final.ipynb)
        - Similar to the previous experimental attempt, but this time the labels determined to be used were better and more accurate solely because it came as a metadata from the original data source itself hence, labelling used was far reliable and resulted in far better classification performance on downstream task. Essentially, the same dataset [dataset.json](./src/data/dataset.json) was used but labelling was done such that it be a binary classification problem: `['linux', 'windows']` and on the basis of if the original content came from a `*.bat` file it was labelled as `'windows'` else if it came from a `*.sh` or `Dockerfile` it be labelled as `'linux'`. This approach worked quite well and resulted in providing a promising classifier. SVM was seen to perform better on the dataset than Naive Bayes, which is why the SVM classification pipeline (included BOW unigram tokenizer, TFIDF weighting pre-processing) was saved to disk for re-use in later steps.
3. Inverted Index Creation for Text Retrieval
    - Script for inverted index creation: [**04-create_ir_idx.py**](./src/04-create_ir_idx.py)
        - An inverted index for text retrieval was constructed using MeTaPy with document contents from the same [dataset.json](./src/data/dataset.json) flattened into a [dataset.dat](./src/data/dataset/dataset.dat) file first, followed by the index being stored to disk in the [idx directory](./src/idx/). The inverted index created is used with Okapi BM25 ranking algorithm in a later step.
4. Web Application
    - Script containing implementation of the web app: [**05-server.py**](./src/05-server.py)
        - The implementation of the web app uses Flask python framework and is viable to run on any web server that supports WSGI interfacing. For this project, `gunicorn` is used to run the webserver.
        - Python functions used:
            - `def search_query(query)`: retrieves top 6 relevant documents with the help of MeTaPy Okapi BM25 for given query using inverted index `idx` at runtime
            - `def classify_query(query)`: returns the predicted probabilities of `['linux', 'windows']` class labels using inference at runtime from persisted scikit-learn `model`
            - `def search_and_classify(query)`: returns a combination of results from both `search_query()` and `classify_query()` function class
            - `def index()`: returns html content templated and values filled in on the basis of the above function calls.
                - "GET /" treated as homepage and shows the input HTML form (templated from [index.html](./src/templates/index.html))
                - "POST /" treated as form submission action and shows the output of results (templated from [results.html](./src/templates/results.html))
            - `app`: the variable containing the Flask app, which is used by WSGI interface of `gunicorn` to run the web app
        - Functional interface of web UI:
            - User is shown a large search bar as an HTML form where user can input their query string which could either be entire script, few keywords from a script or a single line from a script
            - Upon form submission, the output page showcases a bar chart illustrating classification with prediction probabilities and additionally, it presents the top 6 relevant scripts retrieved from the dataset with their corresponding GitHub links.
                - (PS: some GitHub links may not be functional (leading to 404s )as data collection at the time of original source dataset generation isn't the same at inference time on the webapp, online text retrieval isn't included in the scope)
        
## Usage

**Option 1**: Run the web application locally (at http://localhost:5000/).

```sh
# pre-requisite: git, ensure python 3.5/3.6/3.7 is available on local
git clone https://github.com/swghosh/cs410-project.git
cd cs410-project/src
pip install -r requirements.txt
export PORT=5000
gunicorn --bind :$PORT --workers 1 05-server:app
# open http://localhost:5000/ in a browser
```

**Option 2**: Run the web application by deploying it to Google App Engine.

- Pre-requisite: git, an active Google Cloud account with AppEngine enabled, `gcloud` tool setup on local and `gcloud auth login` already done with associated Google account. 
- Ideally, this web app should not consume resources beyond the [Google App Engine Free Tier](https://cloud.google.com/free/docs/free-cloud-features#app-engine) but in case of excessive traffic to the app or in any many other unforeseen cases, **deploying the app may cause charging your Google Cloud account**. Please be aware of the charges that could incur before attempting to deploy the app to your own account.
- Besides the project have been deployed by the author, which can be accessed from **https://code-search-dot-code-crafts-1477836554331.el.r.appspot.com/**.

```sh
git clone https://github.com/swghosh/cs410-project.git
cd cs410-project/src
gcloud config set project "<PROJECT_ID>" # replace with the exact GCP project id where app is intended to be deployed
gcloud app deploy
# open the URL displayed by the output of the last command in a browser
```

## Sample Evaluation Test Cases 

These are some of the sample queries that can one try on the web UI for testing both classification and retrieval.

- Windows
    - `msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi`
    - `REM Breakpad symbols %CMAKE% -E remove_directory %INSTALLSYMDIR%`
    - `cls`
    - `cmd.exe`
    - `set CYGWIN_VERSION`
    - `powershell`
    - `C:\Users`
    - `C:\Windows`
    - `xcopy /s`
    - `ProgramFiles (x86)`
- Linux
    - `sudo apt install git`
    - `kubectl get nodes`
    - `runc`
    - `grep hi`
    - `fish bash sh`
    - `kubeadm init`
    - `linux/amd64`
    - `uname -a`
    - `apk add git`
    - `dnf install gnome`

## Challenges and Limitations

TODO