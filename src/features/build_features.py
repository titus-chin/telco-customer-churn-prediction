import pandas as pd
from sklearn.model_selection import train_test_split
from src.data.utils import load_config, get_project_root
from src.features.min_max_scaler import create_scaler, load_scaler, normalization


def main(
    interim_data_path,
    x_train_path,
    y_train_path,
    x_test_path,
    y_test_path,
    scaler_filepath,
    target_attribute,
    test_size,
):
    data = pd.read_csv(interim_data_path)
    features = data.drop(target_attribute, axis=1)
    target = data[target_attribute]
    features = pd.get_dummies(features)
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=test_size, random_state=0
    )
    create_scaler(x_train, scaler_filepath)
    scaler = load_scaler(scaler_filepath)
    x_train = normalization(scaler, x_train)
    x_train.to_csv(x_train_path, index=False)
    y_train.to_csv(y_train_path, index=False)
    x_test.to_csv(x_test_path, index=False)
    y_test.to_csv(y_test_path, index=False)


if __name__ == "__main__":
    conf = load_config("conf", "parameters", "features.yaml")
    interim_data_path = get_project_root().joinpath(
        "data", "interim", conf["interim_data"]
    )
    x_train_path = get_project_root().joinpath("data", "processed", conf["x_train"])
    y_train_path = get_project_root().joinpath("data", "processed", conf["y_train"])
    x_test_path = get_project_root().joinpath("data", "processed", conf["x_test"])
    y_test_path = get_project_root().joinpath("data", "processed", conf["y_test"])
    scaler_filepath = get_project_root().joinpath("models", conf["scaler_file"])
    main(
        interim_data_path,
        x_train_path,
        y_train_path,
        x_test_path,
        y_test_path,
        scaler_filepath,
        target_attribute=conf["target_attribute"],
        test_size=conf["test_size"],
    )
