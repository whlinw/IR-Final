import pandas as pd
import json

f = open("./demo_data","r")

df = pd.read_csv(f,  sep=',')

print df
big_station_json = {}

for i in range(2, df.shape[1]):
    id = i-1
    print id
    lst = []
    for j in range(0, df.shape[0]):
        lst.append(df.ix[j,i])
    big_station_json[id] = lst
    # g = open("./demo_station_dataset/"+str(id), "w")
    # json.dump({"data":lst}, g)
    # g.close()

g = open("./demo_station_dataset/big_station_json", "w")
json.dump(big_station_json, g)
g.close()

