import numpy as np
import pandas as pd
import csv

def get_data_frames(file, log=True):
    data_frames = {}
    csvfile = open(file,'r')
    csvFileArray = []
    for row in csv.reader(csvfile, delimiter = ';'):
        if row:
            if row[1]:
                csvFileArray.append(row)

    for i in range(0,csvFileArray.__len__()-1, 2):
        if log:
            print("loading od flow:",csvFileArray[i+1][0])
        df = pd.DataFrame({'t':csvFileArray[i][1:-1],'v':csvFileArray[i+1][1:-1]})
        df.v = pd.to_numeric(df.v)
        df.v = pd.to_numeric(df.v/1000000000)
        df.t = pd.to_datetime(df.t, format='%Y-%m-%d_%H:%M:%S', errors='coerce')
        df.index = df.t
        del df['t']
        # s = pd.Series(df.v.values, index=df['t'].values)
        data_frames[csvFileArray[i+1][0]] = df

    csvfile.close()

    return data_frames

