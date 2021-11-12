from sklearn.metrics import recall_score


def recall(model, x, y):
    y_pred = model.predict(x)
    return recall_score(y, y_pred)
