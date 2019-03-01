import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('Classified Data', index_col=0)
print(df.head())

#Para utiizar o KNN é importantissimo realizar a normalização dos valores

scaler = StandardScaler()
#Normaliza tudo, menos o target class, pois será nosso objeto.
scaler.fit(df.drop('TARGET CLASS', axis=1))
df_normalizado = scaler.transform(df.drop('TARGET CLASS', axis=1))
print(df_normalizado)
#Coloca as colunas
df_param = pd.DataFrame(df_normalizado, columns = df.columns[:-1])
print(df_param.head())

x_train, x_test, y_train, y_test = train_test_split(df_param, df['TARGET CLASS'], test_size=0.3)
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)
print(classification_report(y_test, predictions))

#Para buscar o número ideal de vizinhos:
error_rate = []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(x_train, y_train)
    predictions = knn.predict(x_test)
    error_rate.append(np.mean(predictions != y_test))


plt.figure(figsize=(12,6))
plt.plot(range(1,40), error_rate)
plt.show()


knn = KNeighborsClassifier(n_neighbors = 34)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)
    
print(classification_report(y_test, predictions))
