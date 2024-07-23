# src/app.py
import sys
import os
import time
import pandas as pd

# Add the parent directory of `src` to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from weather_api import get_weather
from data_processing import process_weather_data
from database import session, Weather
from config import INTERVAL, CITIES, THRESHOLD_TEMP
from aggregates import daily_summary, check_thresholds

def main():
    while True:
        for city in CITIES:
            data = get_weather(city)
            processed_data = process_weather_data(data)
            weather = Weather(**processed_data)
            session.add(weather)
            session.commit()

            # Load data into a DataFrame for aggregation
            df = pd.read_sql(session.query(Weather).statement, session.bind)
            daily_agg = daily_summary(df)
            alerts = check_thresholds(df, THRESHOLD_TEMP)

            # Optionally, print daily summaries and alerts
            print(daily_agg)
            print(alerts)

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()





# import time
# import pandas as pd
# from weather_api import get_weather
# from data_processing import process_weather_data
# from database import session, Weather
# from config import INTERVAL, CITIES, THRESHOLD_TEMP
# from aggregates import daily_summary, check_thresholds

# def main():
#     while True:
#         for city in CITIES:
#             data = get_weather(city)
#             processed_data = process_weather_data(data)
#             weather = Weather(**processed_data)
#             session.add(weather)
#             session.commit()

#             # Load data into a DataFrame for aggregation
#             df = pd.read_sql(session.query(Weather).statement, session.bind)
#             daily_agg = daily_summary(df)
#             alerts = check_thresholds(df, THRESHOLD_TEMP)

#             # Optionally, print daily summaries and alerts
#             print(daily_agg)
#             print(alerts)

#         time.sleep(INTERVAL)

# if __name__ == "__main__":
#     main()
