import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    API_KEY = os.getenv("API_KEY")
    API_CITY= os.getenv("API_CITY")
    EXCEL_PATH = "weather_data.xlsx"
