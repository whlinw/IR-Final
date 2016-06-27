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
ans = []

with open('../data_sets/mrtOut.csv', 'rb') as mrtOut:
    moReader = csv.reader(mrtOut, delimiter=',')
    next(moReader, None)
    i = 0
    for row in moReader:
        if i < 456:
            data.append(float(row[testStation]))
            i += 1
        else:
            ans.append(float(row[testStation]))

arima_mod = sm.tsa.ARIMA(data, (14, 0, 2)).fit()

params = arima_mod.params
current = len(data)
future = arima_mod.predict(current, current + 29)

with open('./predictApril' + str(testStation) + '.csv', 'wb+') as arimaResult:
    arWriter = csv.writer(arimaResult, delimiter=',')
    arWriter.writerow(future)
    arWriter.writerow(ans)
