from sklearn import svm
from numpy import np
X =
y = [0, 4, 6, 12]
clf = svm.SVR()
print clf
clf.fit(X, y)

print clf.predict([[1, 1]])
print clf.score([[1,2],[3,4]],[3,7])