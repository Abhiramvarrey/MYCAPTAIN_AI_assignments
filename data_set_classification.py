# -*- coding: utf-8 -*-
"""Data_set_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dETS6AUyKtWaAjYl6j6yn93P6k27RnrS
"""

import sys
import pandas as pd
import scipy
import numpy as np
import sklearn
import matplotlib
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names=['sepal-length','sepal-width','petal-length','petal-width','class']
data=pd.read_csv(url,names=names)

data.head()

data.shape

data.describe()

data.groupby('class').size()

data.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
plt.show()

data.hist()
plt.show()

scatter_matrix(data)
plt.show()

array=data.values
x=array[:,0:4]
y=array[:,4]
x_train,x_validation,y_train,y_validation=train_test_split(x,y,test_size=0.2,random_state=1)

models=[]
models.append(('LR',LogisticRegression(solver='liblinear',multi_class='ovr')))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('DTC',DecisionTreeClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM',SVC(gamma='auto')))

results={}
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)
    cv_result = cross_val_score(model, x_train, y_train, cv=kfold, scoring='accuracy')
    results[name]=cv_result
    print('%s: %f (%f)' % (name, cv_result.mean(), cv_result.std()))

plt.boxplot(results.values(), labels=results.keys())
plt.title('Algorithm Comparison')
plt.show()

model = SVC(gamma='auto')
model.fit(x_train, y_train)
predictions = model.predict(x_validation)

#evaluate
print(accuracy_score(y_validation, predictions))
print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))

