import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

iris = sns.load_dataset('iris')
print(iris.head())

sns.pairplot(iris, hue='species', diag_kind = 'hist')
plt.show()
sns.kdeplot(iris[iris['species']=='setosa']['sepal_width'], iris[iris['species']=='setosa']['sepal_length'], cmap='plasma', shade=True, shade_lowest=False)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(iris.drop('species', axis=1), iris['species'], test_size=0.3, random_state=101)
svc = SVC(gamma='auto')
svc.fit(x_train, y_train)
predictions = svc.predict(x_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

param_grid = {'C':[0.1,1,10,100,1000], 'gamma':[1,0.1,0.01,0.001,0.0001], 'kernel':['rbf']}
grid = GridSearchCV(SVC(), param_grid, refit = True, verbose=3)
grid.fit(x_train, y_train)
predictions = grid.predict(x_test)
print(grid.best_params_)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
