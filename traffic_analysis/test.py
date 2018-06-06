# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import process_csv
import textwrap as tw
import fbprophet

from statsmodels.tsa.stattools import adfuller

def test_stationarity(timeseries):

    #Determing rolling statistics
    #pd.rolling_mean(timeseries, window=7*120)
    rolmean = timeseries.rolling(window=7*24*12).mean()
    #pd.rolling_std(timeseries, window=7*120)
    rolstd = timeseries.rolling(window=7*24*12).std()

    #Plot rolling statistics:
    # orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries.v, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
         dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)

file_small = "traffic_ex_small_data.csv"
file = "traffic_ex_data.csv"
indent=5*' '+"---"

data_frames = process_csv.get_data_frames(file_small, False)
#data_frames = process_csv.get_data_frames(file)

# sFB = data_frames['Facebo-d5dc01 (B)']
# print(type(sFB))
# print(sFB)
# plt.figure()
# test_stationarity(sFB)
# plt.show()
def zeros(ts):
    zero_ts = ts[ts==0.0]
    print(indent,"zeros count", len(zero_ts))
    return(not zero_ts.empty)

def size(ts):
    zero_ts = ts[ts==0.0]
    print(indent,"zeros count", len(zero_ts))
    return(not zero_ts.empty)

def process(ts):
    print(indent,type(ts))
    print(indent,ts.index)
    print(indent,ts.values)
    #print(indent,ts.head(5))
    print(indent,ts[1])
    print(indent,ts[3])
    print(indent,zeros(ts))

def process_data(data_frames, max_nb_ts=len(data_frames)):
    i = 0
    for flow_name, s in data_frames.items():
        print(3*'*',"Flow", flow_name)
        zeros(s)
        print(tw.indent(s.describe(include='all').to_string(), prefix = indent+" "))
        # print(type(s.index.to_series()))
        # print(tw.indent((s.index.to_series()).describe().to_string(), prefix = indent+" "))
        gm_prophet = fbprophet.Prophet(changepoint_prior_scale=0.15, weekly_seasonality=True, daily_seasonality=True)
        gm_prophet.fit(s)
        future = gm_prophet.make_future_dataframe(periods=365)
        print(future.tail())
        forecast = gm_prophet.predict(future)
        print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
        gm_prophet.plot(forecast);
        gm_prophet.plot_components(forecast);
        i+=1
        if i==max_nb_ts:
            break

process_data(data_frames, max_nb_ts=1)

    #plt.figure()
    #break
    #print(s[2:5])
    #print(s.tail(10))
    #print(type(s))
    #print(s["2018-05",])
    # print(s.describe(include='all'))
    # mavg = s.rolling(window=1*240).mean()
    # print(s.index)
    # print(s)
    # print(s.min())
    # print(s.max())
    # plt.plot(s, label=flow_name)
    # plt.plot(mavg, label=flow_name)
    #test_stationarity(s)
    #plt.legend(loc='best')
    #plt.show()






