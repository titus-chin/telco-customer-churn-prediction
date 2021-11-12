import wandb
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import cross_val_score
from src.data.utils import get_project_root, load_config
import os


def main():
    wandb.init(group=group, config=default_config)
    model = DummyClassifier(
        random_state=wandb.config.random_state, strategy=wandb.config.strategy
    )
    scores = cross_val_score(model, x_train, y_train, cv=cv, scoring=metric)
    wandb.log({log_metric: scores.mean()})


if __name__ == "__main__":
    wandb_credentials = load_config("conf", "credentials", "wandb.yaml")
    general_conf = load_config("conf", "parameters", "models.yaml")["general_config"]
    model_conf = load_config("conf", "parameters", "models.yaml")["dummy_classifier"]

    os.environ["WANDB_API_KEY"] = wandb_credentials["WANDB_API_KEY"]
    os.environ["WANDB_PROJECT"] = wandb_credentials["WANDB_PROJECT"]
    os.environ["WANDB_ENTITY"] = wandb_credentials["WANDB_ENTITY"]

    x_train_path = get_project_root().joinpath(
        "data", "processed", general_conf["x_train"]
    )
    y_train_path = get_project_root().joinpath(
        "data", "processed", general_conf["y_train"]
    )
    x_train = pd.read_csv(x_train_path)
    y_train = pd.read_csv(y_train_path)

    cv = general_conf["cv"]
    metric = general_conf["metric"]
    log_metric = general_conf["log_metric"]

    group = model_conf["group"]
    default_config = model_conf["default_config"]
    sweep_id = wandb.sweep(model_conf["sweep_config"])

    wandb.agent(sweep_id, function=main)
    wandb.finish()
