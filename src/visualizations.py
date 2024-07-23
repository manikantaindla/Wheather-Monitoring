import matplotlib.pyplot as plt

def plot_daily_summary(daily_agg):
    fig, ax = plt.subplots()
    daily_agg['temp_mean'].plot(kind='line', ax=ax, label='Mean Temp')
    daily_agg['temp_max'].plot(kind='line', ax=ax, label='Max Temp')
    daily_agg['temp_min'].plot(kind='line', ax=ax, label='Min Temp')
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (C)')
    ax.legend()
    plt.show()
