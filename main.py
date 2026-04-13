from services.openweather_api import get_weather
from services.excel_files import save_to_excel

import time


while True:
    weather = get_weather("radom")
    save_to_excel([weather])
    print("Pobieram i zapisuje dane")
    time.sleep(10)

