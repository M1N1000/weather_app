import pandas as pd


def save_to_excel(data):
    try:
        df = pd.DataFrame(data)
        df.to_excel('weather_data.xlsx')

    except Exception as e:
        print(e)



