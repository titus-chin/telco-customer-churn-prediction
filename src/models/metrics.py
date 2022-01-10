from sklearn.metrics import recall_score


def recall(model, x, y):
    """Calculate model recall.

    Parameters
    ----------
    model : sklearn machine learning model
        A machine learning model created using sklearn
    x : pd.DataFrame
        DataFrame containing features
    y : pd.DataFrame
        DatFrame containing target

    Returns
    -------
    float
    """
    y_pred = model.predict(x)
    return recall_score(y, y_pred)
