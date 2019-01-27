import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv('USA_Housing.csv')

print(df.info())
print(df.columns)

sns.pairplot(df)
plt.show()
sns.heatmap(df.corr())
plt.show()
x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
print(x)
y = df['Price']


#Divide o x e o y para criar os DF de treinamento e de teste.
#O tamaanho dos df é de acordo com o test_size
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.4, random_state=101)
print(x_train.shape[0])
print(x_test.shape[0])

lm = LinearRegression()
lm.fit(x_train, y_train)
#Inicio da reta no Y
print(lm.intercept_)
#Coeficientes
print(lm.coef_)

coefs = pd.DataFrame(lm.coef_, x.columns, ['Coefs'])
print(coefs)

predict = lm.predict(x_test)
#Valor real pelo valor previsto
plt.figure(figsize=(14,7))
plt.scatter(x=y_test, y=predict)
plt.show()
#Printa o erro
sns.distplot(y_test-predict)
plt.show()


#Erros
print("MAE", metrics.mean_absolute_error(y_test, predict))
print("MSE", metrics.mean_squared_error(y_test, predict))
print("RMSE", np.sqrt(metrics.mean_squared_error(y_test, predict)))
