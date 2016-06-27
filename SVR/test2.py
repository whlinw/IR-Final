from sklearn import svm
import numpy as np

X =[[-1,-1],[2,2],[3,3],[7,7]]
y = [-2, 4, 6, 14]

# theta0 + x1*theta1 + x2*theta2 = y

clf = svm.SVR(en)
clf.fit(X, y)
print clf

print clf.predict([[1, 1]])

print clf.score([[1,2],[3,4]],[4,6])