import pandas as pd
import openpyxl
import os
from config import Config


def save_to_excel(data):
    PATH = Config.EXCEL_PATH

    try:
        new_df = pd.DataFrame(data)
        if os.path.exists(PATH):
            current = pd.read_excel(PATH)
            concat_data = pd.concat([current, new_df], ignore_index=True)
            concat_data.to_excel(PATH, index=False)
        else:
            new_df.to_excel(PATH, index=False)

    except Exception as e:
        print(e)

def read_excel(filepath):
    try:
        df = pd.read_excel(filepath)
        return df

    except Exception as e:
        print(e)
