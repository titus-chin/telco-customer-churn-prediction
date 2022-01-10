from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import joblib


def create_scaler(x_train, scaler_filepath):
    """Create MinMaxScaler save object from training features.

    Parameters
    ----------
    x_train : pd.DataFrame
        DataFrame containing training features
    scaler_filepath : pathlib.PosixPath
        Path to MinMaxScaler save object
    """
    scaler = MinMaxScaler()
    scaler.fit(x_train)
    joblib.dump(scaler, scaler_filepath)


def load_scaler(scaler_filepath):
    """Load MinMaxScaler save object.

    Parameters
    ----------
    scaler_filepath : pathlib.PosixPath
        Path to MinMaxScaler save object

    Returns
    -------
    sklearn.preprocessing._data.MinMaxScaler
    """
    return joblib.load(scaler_filepath)


def normalization(scaler, features):
    """Normalize features using fitted MinMaxScaler.

    Parameters
    ----------
    scaler : sklearn.preprocessing._data.MinMaxScaler
        Fitted MinMaxScaler object
    features : pd.DataFrame
        DataFrame containing features

    Returns
    -------
    pd.DataFrame
    """
    return pd.DataFrame(scaler.transform(features), columns=features.columns)
