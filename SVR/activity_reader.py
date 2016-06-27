import pandas as pd
import csv
import os
import json
from datetime import timedelta
from datetime import date
from datetime import datetime


def readjson():
    f = open("../data_sets/activity.json", "r")
    dict = json.load(f)
    f.close()
    return dict

def readDictAllKeys(dict):
    key_sets = set()
    for key, val in dict.iteritems():
        for c in val:
            key_sets.add(c["keyword"])
    return list(key_sets)


def jsonToDF(dict, start, end, index, key_list):
    print "hi"
    columns = ["datetime", "activity"] + key_list
    df = pd.DataFrame(columns=columns)

    cur_date = start
    datetime_list = []
    while cur_date <= end:
        datetime_list.append(cur_date)
        cur_date += timedelta(days=1)

    df['datetime'] = datetime_list

    df = df.fillna(0)

    if str(index) in dict:
        id_contentlist = dict[str(index)]
        for content in id_contentlist:
            date = datetime.strptime(content['date'],"%Y-%m-%d").date()
            keyword = content['keyword']
            df.loc[df['datetime'] == date, 'activity'] = 1
            df.loc[df['datetime'] == date, keyword] = 1

    return df

def main_specificTime(start, end, index):
    dict = readjson()
    key_list = readDictAllKeys(dict)
    df = jsonToDF(dict, start, end, index, key_list)
    del df["datetime"]
    return df

if __name__ == "__main__":
    df = main_specificTime(date(year=2015,month=7,day=1),date(year=2015,month=8,day=1), 15)
    print df





