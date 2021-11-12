from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import joblib


def create_scaler(x_train, scaler_filepath):
    scaler = MinMaxScaler()
    scaler.fit(x_train)
    joblib.dump(scaler, scaler_filepath)


def load_scaler(scaler_filepath):
    return joblib.load(scaler_filepath)


def normalization(scaler, features):
    return pd.DataFrame(scaler.transform(features), columns=features.columns)
