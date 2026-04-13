import pandas as pd

from config import Config


def save_to_excel(data):
    PATH = Config.EXCEL_PATH

    try:
        df = pd.DataFrame(data)
        df.to_excel('weather_data.xlsx')

    except Exception as e:
        print(e)



