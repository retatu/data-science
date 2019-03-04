import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

cancer = load_breast_cancer()
print(cancer.keys())

df = pd.DataFrame(cancer['data'], columns = cancer['feature_names'])
print(df.head())
df_target = pd.DataFrame(cancer['target'], columns = ['Cancer'])
x_test, x_train, y_test, y_train = train_test_split(df, np.ravel(df_target), test_size = 0.3, random_state = 101)

svc = SVC(gamma='auto')
svc.fit(x_train, y_train)
predictions = svc.predict(x_test)
#Resultados muito ruins
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

#É tipo um auto treino, onde ele vai trocando os parâmetros e retreinando
#E então ele adiciona um score para cada teste.
param_grid = {'C':[0.1,1,10,100,1000], 'gamma':[1,0.1,0.01,0.001,0.0001], 'kernel':['rbf']}
grid = GridSearchCV(SVC(), param_grid, refit = True, verbose=3)
grid.fit(x_train, y_train)
#Os melhores parâmetros encontrados
print(grid.best_params_)
#E então testa novamente
predictions = grid.predict(x_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
