import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv('kyphosis.csv')
print(df.info())
print(df.head())

#Verificar se existe separação dos dados
sns.pairplot(df, hue='Kyphosis', diag_kind='hist')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(df.drop('Kyphosis', axis=1), df['Kyphosis'], test_size = 0.3)
#Arvore de decisão
decision_tree = DecisionTreeClassifier()
decision_tree.fit(x_train, y_train)
predict = decision_tree.predict(x_test)

print(classification_report(y_test, predict))
print(confusion_matrix(y_test, predict))
#Florestas aleatórias
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(x_train, y_train)
predict = rfc.predict(x_test)

print(classification_report(y_test, predict))
print(confusion_matrix(y_test, predict))
