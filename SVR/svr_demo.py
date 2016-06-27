import numpy as np
from sklearn import svm
from datetime import date
import numpy as np
from sklearn import grid_search
from sklearn import preprocessing

import csv

import data_sets.weather_reader as weather_reader

# "index" is id of metro station
def read_Ydata(index):

    y_data = []
    with open('data_sets/mrtOut.csv', 'r') as mrtOut:
        moReader = csv.reader(mrtOut, delimiter=',')
        next(moReader, None)
        for row in moReader:
            y_data.append(float(row[index]))
    y_data = np.array(y_data)
    return y_data

def read_Weather(start, end):
    df = weather_reader.main_specificTime(start,end,cache=False)

    # print df
    x_data = preprocessing.scale(df.as_matrix())
    return x_data


def svr_train(index):

    train_y = read_Ydata(index)
    train_x = read_Weather(date(year=2015,month=1,day=1),date(year=2016,month=4,day=30))




    # clf = svm.SVR()
    svr = svm.SVR()
    param_grid = {
        'C': [0.001, 0.01, 0.1, 1, 10, 100],
        'epsilon': [0.00001, 0.001, 0.01, 0.1],
        'gamma': [0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4]
    }
    clf = grid_search.GridSearchCV(svr, param_grid)
    clf.fit(train_x, train_y)
    return clf

def svr_predict(index):

    clf = svr_train(index)

    test_x = read_Weather(date(year=2016,month=5,day=1),date(year=2016,month=6,day=30))
    tested_y = clf.predict(test_x)

    return tested_y


if __name__ == "__main__":
    print svr_predict(1)