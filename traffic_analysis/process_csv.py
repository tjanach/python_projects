import pandas as pd
import csv
file_small = "traffic_ex_small_data.csv"
file = "traffic_ex_data.csv"
#pd.read_csv(file, sep=';').T.to_csv('traffic_ex_small_data_t.csv',header=False, sep=';')

#red_file = pd.read_csv(file, sep=';')

#print(red_file.head(10))

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
        df.v = pd.to_numeric(df.v/1000000)
        df.t = pd.to_datetime(df.t, format='%Y-%m-%d_%H:%M:%S', errors='coerce')
        data_frames[csvFileArray[i+1][0]] = df

    csvfile.close()

    return data_frames

data_frames = get_data_frames(file)
for flow_name, df in data_frames.items():
     print(3*'*',"Flow", flow_name)
     print(df.v.describe())

# csvfile = open(file,'r')
# csvFileArray = []
# for row in csv.reader(csvfile, delimiter = ';'):
#     #print(row)
#     if row:
#         #print('not_empty',row)
#         if row[1]:
#             csvFileArray.append(row)
#
# print(type(csvFileArray))
# print(csvFileArray.__len__())
# for i in range(0,csvFileArray.__len__()-1, 2):
#     print(i,len(csvFileArray[i]))
#     df =pd.DataFrame({'t':csvFileArray[i][1:-1],'v':csvFileArray[i+1][1:-1]})
#     for j in range(0,len(csvFileArray[i])-1):
#         print(csvFileArray[i][j]+'  '+csvFileArray[i+1][j])
#         #print()
#
# print(df.t)
# df.v = pd.to_numeric(df.v)
# df.v = pd.to_numeric(df.v/1000000)
# df.t = pd.to_datetime(df.t, format='%Y-%m-%d_%H:%M:%S', errors='coerce')
# print(df.dtypes)
# print(df)

#print(df.values)
#for r in csvFileArray:
#    print(r)
#print(csvFileArray[0])
#print(csvFileArray[1])
#print(csvFileArray[2])
#print(csvFileArray[3])
#print(csvFileArray[4])
#print(csvFileArray[5])