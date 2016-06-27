import argparse
from read_MetroOut import read_MetroOut
from SVR.svr_demo import svr_predict
from datetime import date
from datetime import datetime
from datetime import timedelta
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-o", type=str, help="output file")

args = parser.parse_args()
write_path = args.o
f = open(write_path, "w")



past_df = read_MetroOut()

for i in range(0, past_df.shape[0]):
    past_df.ix[i, 0] = datetime.strptime(past_df.ix[i,0], '%m/%d/%Y').date()

cur = date(year=2016, month=5, day=1)
past_len = past_df.shape[0]
while(cur <= date(year=2016,month=6,day=30)):
    past_df.loc[past_df.shape[0]] = [cur]+[0]* (past_df.shape[1]-1)
    cur +=  timedelta(days=1)


for i in range(1, 108):
    lst = svr_predict(i)
    for j in range(0, len(lst)):
        past_df.ix[past_len+j, i] = lst[j]
    print "complete:i", i
    past_df.to_csv("demo_data")






