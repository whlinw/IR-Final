import numpy as np
from sklearn import svm
from datetime import date
import numpy as np
from sklearn import grid_search
from sklearn import preprocessing

import csv

import weather_reader
import activity_reader
import vacation_reader

# "index" is id of metro station
def read_Ydata(index):

    y_data = []
    with open('../data_sets/mrtOut.csv', 'r') as mrtOut:
        moReader = csv.reader(mrtOut, delimiter=',')
        next(moReader, None)
        for row in moReader:
            y_data.append(float(row[index]))
    y_data = np.array(y_data)
    return y_data

def read_Weather(start, end):
    df = weather_reader.main_specificTime(start,end,cache=False)

    x_data = preprocessing.scale(df.as_matrix())
    return x_data

def read_Activity(start, end, index):
    df = activity_reader.main_specificTime(start, end, index)
    x_data = preprocessing.scale(df.as_matrix())
    return x_data


def svr_train(index):

    y_data = read_Ydata(index)
    train_y = y_data[:456]
    train_x = read_Weather(date(year=2015,month=1,day=1),date(year=2016,month=3,day=31))

    # activity
    train_x_activity = read_Activity(date(year=2015,month=1,day=1),date(year=2016,month=3,day=31), index)
    train_x = np.concatenate((train_x, train_x_activity), axis=1)

    # vacation
    train_x_vacation = read_Activity(date(year=2015, month=1, day=1), date(year=2016, month=3, day=31), index)
    train_x = np.concatenate((train_x, train_x_vacation), axis=1)

    clf = svm.SVR(C=100)
    svr = svm.SVR()
    param_grid = {
        'C': [0.001, 0.01, 0.1, 1, 10, 100],
        'epsilon': [0.00001, 0.001, 0.01, 0.1],
        'gamma': [0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4]
    }

    clf = grid_search.GridSearchCV(svr, param_grid)
    # print clf
    clf.fit(train_x, train_y)
    return clf

def svr_predict(clf, index):

    test_x = read_Weather(date(year=2016,month=4,day=1),date(year=2016,month=4,day=30))

    # activity
    test_x_activity = read_Activity(date(year=2016,month=4,day=1),date(year=2016,month=4,day=30), index)
    test_x = np.concatenate((test_x, test_x_activity), axis=1)

    # vacation
    test_x_vacation = read_Activity(date(year=2016, month=4, day=1), date(year=2016, month=4, day=30), index)
    test_x = np.concatenate((test_x, test_x_vacation), axis=1)

    tested_y = clf.predict(test_x)

    return tested_y

def estimation(a, b):
    sum = 0


if __name__ == "__main__":
    clf = svr_train(43)
    print svr_predict(clf, 43)
    print read_Ydata(43)[-30:]