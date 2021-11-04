import pandas as pd
from src.data.utils import load_config, get_project_root


def main(raw_data_path):
    raw_data = pd.read_csv(raw_data_path)
    print(raw_data["Churn"].value_counts(normalize=True))


if __name__ == "__main__":
    conf = load_config("conf", "parameters", "data.yaml")
    raw_data_path = get_project_root().joinpath("data", "raw", conf["raw_data"])
    main(raw_data_path)
