# -*- coding: utf-8 -*-
"""diabaties.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bxo4ptYXkRb0hB0sdl38OV0JMQmKKM7f
"""

import pandas as pd
import numpy as np

data=pd.read_csv('/content/diabetes.csv')
data

data.head()

data.columns

data.columns.isna().sum()

data['BMI'].isna().sum()

columns_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

data[columns_with_zeros] = data[columns_with_zeros].replace(0, np.nan)
data[columns_with_zeros] = data[columns_with_zeros].fillna(data[columns_with_zeros].median())

data

from sklearn.model_selection import train_test_split
X = data.drop('Outcome', axis=1)
y = data['Outcome']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=64)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

X

y

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
import xgboost as xgb
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

knc=KNeighborsClassifier()
rf=RandomForestClassifier()
svc=SVC()
lr=LogisticRegression()
dt=DecisionTreeClassifier()
gnb=GaussianNB()
etc=ExtraTreeClassifier()
xgb=xgb.XGBClassifier()
abc=AdaBoostClassifier()

models = {
    'Logistic Regression':lr,
    'K neighbours classifier':knc,
    'Decision Tree Classifier':dt,
    'Gaussian Naive Bayes':gnb,
    'Extra Tree Classifier':etc,
    'Ada Boost Classifier':abc,
    'XGB Classifier':xgb,
    'Random Forest Classifier':rf,
    'Support Vector Classifier':svc
}


for model_name, model in models.items():
    model.fit(x_train, y_train)
    y_pred = model.predict(x_train)
    report=classification_report(y_train,y_pred)
    print(f"Classification report for {model_name}:\n{report}\n")

