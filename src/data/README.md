Directory containing the contents used during runtime of the webapp.

Current contents include:
- `dataset.json`: pre-processed dataset stored such that it can be serializable into a Pandas Dataframe.
- `model.joblib`: SVM classification pipeline which is serializable with scikit-learn and joblib.
- `dataset/`: contains dataset in the format readable by meta which was used for constructing inverted index. 
- `icons.json`: contains 3 logo icon png files stored in base64 format used statically within the web app.
