import pandas as pd
import json

f = open("./demo_data","r")

df = pd.read_csv(f,  sep=',')

print df

big_dict = {}
for i in range(0, df.shape[0]):
    timestr = df.ix[i, 1]
    print timestr
    dict = {}
    for j in range(2, df.shape[1]):
        dict[j-1] = df.ix[i,j]
    # g = open("./demo_dataset/"+timestr, "w")
    # json.dump(dict, g)
    # g.close()
    big_dict[timestr] = dict

g = open("./demo_dataset/big-json", "w")
json.dump(big_dict, g)
g.close()


