import pandas as pd
from src.data.data_cleaning import drop_columns, change_values
from src.data.utils import load_config, get_project_root


def main(
    raw_data_path,
    interim_data_path,
    columns_to_drop,
    columns_to_change,
):
    """Pipeline to produce interim data from raw data.

    Parameters
    ----------
    raw_data_path : pathlib.PosixPath
        Path to raw data
    interim_data_path : pathlib.PosixPath
        Path to interim data
    columns_to_drop : list
        List of columns to drop
    columns_to_change : dict
        Dictionary containing columns to change and values to replace
    """
    data = pd.read_csv(raw_data_path)
    drop_columns(data, columns_to_drop)
    change_values(data, columns_to_change)
    data.to_csv(interim_data_path, index=False)


if __name__ == "__main__":
    conf = load_config("conf", "parameters", "data.yaml")
    raw_data_path = get_project_root().joinpath("data", "raw", conf["raw_data"])
    interim_data_path = get_project_root().joinpath(
        "data", "interim", conf["interim_data"]
    )
    main(
        raw_data_path,
        interim_data_path,
        columns_to_drop=conf["columns_to_drop"],
        columns_to_change=conf["columns_to_change"],
    )
