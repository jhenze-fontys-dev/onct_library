# onct/data.py

import json
import pandas as pd


def print_json(data, max_characters=4000):
    """
    Print JSON data in a readable format.

    Example:
        print_json(data)
    """

    text = json.dumps(data, indent=2)

    if len(text) > max_characters:
        print(text[:max_characters])
        print("\n... output shortened ...")
    else:
        print(text)


def save_json(data, filename):
    """
    Save JSON data to a file.

    Example:
        save_json(data, "data/meta_30d.json")
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_json(filename):
    """
    Load JSON data from a file.

    Example:
        data = load_json("data/meta_30d.json")
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def json_to_dataframe(
    data,
    record_path=None,
    numeric_columns=None,
    datetime_columns=None,
):
    """
    Convert JSON data to a pandas DataFrame.

    Args:
        data (dict | list): JSON data.
        record_path (str | None): Key where the records are stored.
        numeric_columns (list[str] | None): Columns to convert to numbers.
        datetime_columns (list[str] | None): Columns to convert to dates.

    Example:
        df = json_to_dataframe(
            data,
            record_path="values",
            numeric_columns=["open", "high", "low", "close", "volume"],
            datetime_columns=["datetime"]
        )
    """

    if record_path is not None:
        if record_path not in data:
            raise ValueError(f"JSON data does not contain '{record_path}'.")

        rows = data[record_path]
    else:
        rows = data

    df = pd.DataFrame(rows)

    if datetime_columns:
        for column in datetime_columns:
            df[column] = pd.to_datetime(df[column])

    if numeric_columns:
        for column in numeric_columns:
            df[column] = pd.to_numeric(df[column])

    return df