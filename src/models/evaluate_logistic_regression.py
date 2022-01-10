from src.features.min_max_scaler import load_scaler, normalization
from src.data.utils import load_config, get_project_root
from src.models.metrics import recall
import pandas as pd
import wandb
from sklearn.linear_model import LogisticRegression
import pickle
import os


def main(
    x_train, y_train, x_test, y_test, name, best_config, metric, scaler, model_filepath
):
    """Evaluate the performance of best logistic regression classifier,
    record the performance to Weights & Biases dashboard, and save
    the model object.

    Parameters
    ----------
    x_train : pd.DataFrame
        DataFrame containing training features
    y_train : pd.DataFrame
        DataFrame containing training target
    x_test : pd.DataFrame
        DataFrame containing testing features
    y_test : pd.DataFrame
        DataFrame containig testing target
    name : str
        Group in Weights and Biases dashboard
    best_config : dict
        Dictionary specifying the best model configuration
    metric : str
        Evaluation metric to evaluate model performance
    scaler : sklearn.preprocessing._data.MinMaxScaler
        Fitted MinMaxScaler object
    model_filepath : pathlib.PosixPath
        Path to model sav object
    """
    wandb.init(name=name, group="Model Performance", config=best_config)
    model = LogisticRegression(
        random_state=wandb.config.random_state,
        C=wandb.config.c,
        solver=wandb.config.solver,
        n_jobs=wandb.config.n_jobs,
        class_weight=wandb.config.class_weight,
    )
    model.fit(x_train, y_train)
    training_recall = recall(model, x_train, y_train)
    x_test = normalization(scaler, x_test)
    testing_recall = recall(model, x_test, y_test)
    wandb.log(
        {f"training_{metric}": training_recall, f"testing_{metric}": testing_recall}
    )
    wandb.finish()
    pickle.dump(model, open(model_filepath, "wb"))


if __name__ == "__main__":
    wandb_credentials = load_config("conf", "credentials", "wandb.yaml")
    general_conf = load_config("conf", "parameters", "models.yaml")["general_config"]
    model_conf = load_config("conf", "parameters", "models.yaml")["logistic_regression"]

    os.environ["WANDB_API_KEY"] = wandb_credentials["WANDB_API_KEY"]
    os.environ["WANDB_PROJECT"] = wandb_credentials["WANDB_PROJECT"]
    os.environ["WANDB_ENTITY"] = wandb_credentials["WANDB_ENTITY"]

    x_train_path = get_project_root().joinpath(
        "data", "processed", general_conf["x_train"]
    )
    y_train_path = get_project_root().joinpath(
        "data", "processed", general_conf["y_train"]
    )
    x_test_path = get_project_root().joinpath(
        "data", "processed", general_conf["x_test"]
    )
    y_test_path = get_project_root().joinpath(
        "data", "processed", general_conf["y_test"]
    )
    x_train = pd.read_csv(x_train_path)
    y_train = pd.read_csv(y_train_path).values.reshape(-1)
    x_test = pd.read_csv(x_test_path)
    y_test = pd.read_csv(y_test_path).values.reshape(-1)

    scaler_filepath = get_project_root().joinpath("models", general_conf["scaler_file"])
    scaler = load_scaler(scaler_filepath)

    model_filepath = get_project_root().joinpath("models", model_conf["model_file"])

    main(
        x_train,
        y_train,
        x_test,
        y_test,
        name=model_conf["group"],
        best_config=model_conf["best_config"],
        metric=general_conf["metric"],
        scaler=scaler,
        model_filepath=model_filepath,
    )
