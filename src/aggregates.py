import pandas as pd

def daily_summary(df):
    daily_agg = df.resample('D', on='dt').agg({
        'temp': ['mean', 'max', 'min'],
        'main': lambda x: x.value_counts().index[0]  # Dominant weather condition
    })
    daily_agg.columns = ["_".join(x) for x in daily_agg.columns.ravel()]
    return daily_agg

def check_thresholds(df, threshold):
    alerts = df[df['temp'] > threshold].copy()
    if not alerts.empty:
        print("Threshold breached:", alerts)
    return alerts
