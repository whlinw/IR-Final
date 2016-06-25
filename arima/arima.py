import csv
import sys
import numpy as np
from scipy import stats
import pandas as pd
#import matplotlib.pyplot as plt

import statsmodels.api as sm
#from statsmodels.graphics.api import qqplot

arguments = sys.argv
testStation = int(arguments[1])
data = []

with open('./data_sets/mrtOut.csv', 'rb') as mrtOut:
    moReader = csv.reader(mrtOut, delimiter=',')
    next(moReader, None)
    for row in moReader:
        data.append(float(row[testStation]))

arima_mod = sm.tsa.ARIMA(data, (7, 0, 2)).fit()
prediction = arima_mod.predict()

with open('./arimaResult' + str(testStation) + '.csv', 'wb+') as arimaResult:
    arWriter = csv.writer(arimaResult, delimiter=',')
    arWriter.writerow(data)
    arWriter.writerow(prediction)
#dist = 0.0
#for i in range(len(prediction)):
#    dist += pow(prediction[i] - data[i], 2)

#dist /= len(prediction)
#print(dist)
