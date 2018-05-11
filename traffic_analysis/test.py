# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import process_csv

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

# data_frames = process_csv.get_data_frames(file_small)
data_frames = process_csv.get_data_frames(file)

# sFB = data_frames['Facebo-d5dc01 (B)']
# print(type(sFB))
# print(sFB)
# plt.figure()
# test_stationarity(sFB)
# plt.show()

for flow_name, s in data_frames.items():
    plt.figure()
    print(3*'*',"Flow", flow_name)
    # print(s.describe(include='all'))
    # mavg = s.rolling(window=1*240).mean()
    # print(s.index)
    # print(s)
    # print(s.min())
    # print(s.max())
    # plt.plot(s, label=flow_name)
    # plt.plot(mavg, label=flow_name)
    test_stationarity(s)
    plt.legend(loc='best')
    plt.show()






