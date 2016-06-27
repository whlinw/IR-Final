import pandas as pd
import csv
import os
import json
from datetime import timedelta
from datetime import date
from datetime import datetime


def readjson():
    f = open("../data_sets/vacation.json", "r")
    dict = json.load(f)
    f.close()
    return dict["data"]

def jsontodf(mylist, start, end):

    df = pd.DataFrame(mylist)

    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    return df[(df["date"] >= start) & (df["date"] <= end)]

def main_specificTime(start, end):
    mylist = readjson()
    df = jsontodf(mylist, datetime(*(start.timetuple()[:6])), datetime(*(end.timetuple()[:6])))
    del df['date']
    return df

if __name__ == "__main__":

    df = main_specificTime(date(year=2015,month=3, day=1), date(year=2015,month=4, day=1))
    print df
    # df = main_specificTime(date(year=2015,month=7,day=1),date(year=2015,month=8,day=1), 15)
    # print df





