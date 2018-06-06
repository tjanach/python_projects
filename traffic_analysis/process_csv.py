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

    for i in range(0,len(csvFileArray)-1, 2):
        if log:
            print("loading od flow:",csvFileArray[i+1][0])
        df = pd.DataFrame({'ds':csvFileArray[i][1:-1],'y':csvFileArray[i+1][1:-1]})
        df.y = pd.to_numeric(df.y)
        df.y = pd.to_numeric(df.y*8/300000000000)
        df.ds = pd.to_datetime(df.ds, format='%Y-%m-%d_%H:%M:%S', errors='coerce')
        df.index = df.ds
        # del df['ds']
        data_frames[csvFileArray[i+1][0]] = df
        #print(type(df))

    csvfile.close()

    return data_frames

