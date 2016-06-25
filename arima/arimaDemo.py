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
current = len(data)
future = arima_mod.predict(current, current + 60)

with open('./arimaDemoResult' + str(testStation) + '.csv', 'wb+') as arimaResult:
    arWriter = csv.writer(arimaResult, delimiter=',')
    arWriter.writerow(future)
