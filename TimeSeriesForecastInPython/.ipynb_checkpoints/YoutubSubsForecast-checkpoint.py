import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Read the data file
ytsubs_df = pd.read_csv('Totals.csv')
print(ytsubs_df.shape)

ytsubs_df.iloc[0,1] = 12

ytsubs_df['TotalSubscribers'] = ytsubs_df['Subscribers'].cumsum()

def forecast_with_Rwf(df,col,h):
    """Calculate and return the forecasts using Naive with Drift method also called random walk forecast method
        Return: forecast - list containing the point forecasts
        Input:  df  - dataframe containing the time series columns
                col - Name of the column in the dataframe containing the time series
                h   - Time period for which to forecast
    """
    y_1 , y_T = df[col].iloc[1] , df[col].iloc[-1]
    T = df[col].shape[0]
    forecast = []
    for h in range(1,31):
        val = y_T + (h*(y_T-y_1)/(T-1))
        forecast.append(int(val))
    return forecast


def generate_date_range(start_date,numdays=30,fmt='%Y-%m-%d',direction='forward'):
    """Generate the date range from given start date for the number days in the given direction
    Input:  start_date - starting date from which to create the date range format expected YYYY-MM-DD
            numdays    - Number of days for which the date range needs to be generated for
            fmt        - date format to be returned
            direction  - forward or backward direction
    """
    base = datetime.datetime.strptime(start_date,'%Y-%m-%d')    
    if direction=='forward':
        date_list = [(base + datetime.timedelta(days=x)).strftime(fmt) for x in range(numdays)]
    elif direction=='backward':#reverese date range
        date_list = [(base - datetime.timedelta(days=x)).strftime(fmt) for x in range(numdays)]
    else:
        print('direction value should be either "forward" or "backward"')
        return None
    return date_list

fcast_rwf = forecast_with_Rwf(ytsubs_df,'TotalSubscribers',30)

fcast_rwf_df = pd.DataFrame({'Date':generate_date_range('2021-01-02'), 'TotalSubscribers':fcast_rwf})

print(fcast_rwf_df)
print(fcast_rwf[-1])
plt.plot(ytsubs_df['TotalSubscribers'])
plt.show()