import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('KNN_Project_Data', index_col=0)
print(df.head())

#sns.pairplot(df, hue='TARGET CLASS', palette='bwr', diag_kind='hist')
#plt.show()

#Para utiizar o KNN é importantissimo realizar a normalização dos valores
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
df_normalizado = scaler.transform(df.drop('TARGET CLASS', axis=1))
df_normalizado = pd.DataFrame(df_normalizado, columns = df.columns[:-1])
print(df_normalizado)

x_train, x_test, y_train, y_test = train_test_split(df_normalizado, df['TARGET CLASS'], test_size = 0.3)

knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

error_rate = []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(x_train, y_train)
    predictions = knn.predict(x_test)
    error_rate.append(np.mean(predictions != y_test))

plt.figure(figsize=(12,6))
plt.plot(range(1,40), error_rate)
plt.show()

#Com 34 vizinhos (como mostrado no gráfico, foi o melhor resultado obtido)
knn = KNeighborsClassifier(n_neighbors = 34)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))











