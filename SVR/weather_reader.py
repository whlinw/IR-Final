import pandas as pd
import csv
import os
from datetime import timedelta
from datetime import date


def readpathdf(path):
    df = pd.read_csv(path, sep=",")
    df.columns = [
        "CST", "Max_Temperature", "Mean_Temperature", "Min_Temperature", "Dew_Point", "MeanDew_Point", "Min_Dewpoint",
        "Max_Humidity", "Mean_Humidity", "Min_Humidity", "Max_Sea_Level_Pressure", "Mean_Sea_Level_Pressure",
        "Min_Sea_Level_Pressure", "Max_Visibility", "Mean_Visibility", "Min_Visibilit", "Max_Wind_Speed",
        "Mean_Wind_Speed", "Max_Gust_Speed", "Precipitation", "CloudCover", "Events", "WindDirDegrees"
    ]

    for name in ["MeanDew_Point", "Min_Dewpoint","Max_Humidity",
                 "Precipitation", "Max_Gust_Speed"]:
        del df[name]

    for index, row in df.iterrows():
        if pd.isnull(row["Events"]):
            df.loc[index, "Events"] = 0
        elif row["Events"] == 'Fog-Rain':
            df.loc[index, "Events"] = 3
        elif row["Events"] == 'Rain':
            df.loc[index, "Events"] = 4
        elif row["Events"] == 'Thunderstorm':
            df.loc[index, "Events"] = 5
        else:
            df.loc[index, "Events"] = 6


    fillna_list = list(df.columns.values)
    fillna_list.remove("CST")
    for column_name in fillna_list:
        df[column_name] = pd.to_numeric(df[column_name])
        df_pad = df[column_name].fillna(method="pad").fillna(method="bfill")
        df_bfill = df[column_name].fillna(method="bfill").fillna(method="pad")
        df[column_name] = df_pad.add(df_bfill) / 2

    return df

def addDatetime(df):
    cur_date = date(year=2015, month=1, day=1)
    datetime_list = []
    for index, row in df.iterrows():
        datetime_list.append(cur_date)
        cur_date += timedelta(days=1)

    df['datetime'] = datetime_list

    weekday = []
    for x in datetime_list:
        if x.weekday() < 5:
            weekday.append(1)
        else:
            weekday.append(0)
    df['weekday'] = weekday

    dayOfWeek = []
    for x in datetime_list:
        dayOfWeek.append(x.weekday()+1)
    df['dayOfWeek'] = dayOfWeek



    del df["CST"]
    return df

def main():
    df_list = []
    for filename in os.listdir("../data_sets/weather_data"):
        df_list.append(readpathdf("../data_sets/weather_data/"+filename))
    df = pd.concat(df_list)
    df = addDatetime(df)

    return df

def main_specificTime(start, end, cache=False):
    import cPickle
    if cache==True:
        try:
            df = cPickle.load("./df_cache")
            return df
        except:
            df = main()
            df = df[df["datetime"] >= start]
            df = df[df["datetime"] <= end]
            del df["datetime"]
            cPickle.dump(df, file("./df_cache","w"))
    else:
        df = main()
        df = df[df["datetime"]>= start]
        df = df[df["datetime"]<= end]
        del df["datetime"]
    return df

if __name__ == "__main__":
    df = main_specificTime(date(year=2015,month=3,day=1),date(year=2015,month=4,day=1))
    print df





