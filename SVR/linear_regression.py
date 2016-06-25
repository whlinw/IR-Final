import numpy as np
from sklearn import svm
from datetime import date
import numpy as np
from sklearn import grid_search
from sklearn import preprocessing
from sklearn import linear_model

import csv

import weather_reader

print "read data"
y_data = []
with open('../data_sets/mrtOut.csv', 'rb') as mrtOut:
    moReader = csv.reader(mrtOut, delimiter=',')
    next(moReader, None)
    for row in moReader:
        y_data.append(float(row[9]))
y_data = np.array(y_data)

df = weather_reader.main_specificTime(date(year=2015,month=1, day=1),
                                 date(year=2016,month=4, day=30),
                                      cache=True)
# x_data = df.as_matrix()
x_data = preprocessing.scale(df.as_matrix())

print "train data"


train_y = y_data[:450]
train_x = x_data[:450,:]
test_y = y_data[-30:]
test_x = x_data[-30:,:]
# train_y = y_data
# train_x = x_data
# test_y = y_data
# test_x = x_data


print train_y.shape
print train_x.shape


# clf = svm.SVR()
clf = linear_model.LinearRegression()
clf.fit(train_x, train_y)
print clf




print test_y.shape
print test_x.shape

print test_y
tested_y = clf.predict(test_x)
print tested_y

# print clf.score(test_x, test_y)
sum = 0
for index in range(0, len(tested_y)):
    sum += (tested_y[index]-test_y[index])**2
print "sum:", sum
print (sum / float(len(tested_y))) ** (0.5)
