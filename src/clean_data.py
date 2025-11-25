import pandas as pd
import glob
import os

def load_all_daily_records(data_folder="../data"):
    """
    Loads all CSV files in the data folder and concatenates them
    into a single pandas DataFrame.
    """

    all_files = glob.glob(os.path.join(data_folder, "*.csv"))

    df_list = []
    for file in all_files:
        temp_df = pd.read_csv(file)
        temp_df["source_file"] = os.path.basename(file)
        df_list.append(temp_df)

    if not df_list:
        raise ValueError("No CSV files found in the data folder.")

    final_df = pd.concat(df_list, ignore_index=True)
    return final_df
