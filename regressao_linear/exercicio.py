import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

pd.set_option('display.max_columns', None)

df = pd.read_csv('ecommerce_customers.csv')
print(df.head())
print(df.info())
print(df.describe())

sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=df)
plt.show()
sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=df)
plt.show()
sns.jointplot(x='Time on App', y='Length of Membership', data=df, kind='hex')
plt.show()
sns.pairplot(df)
plt.show()
#Quanto maior o tempo como membro, indica que gasta mais anualmente
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=df)
plt.show()

x = df[['Avg. Session Length','Time on App','Time on Website','Length of Membership']]
y = df['Yearly Amount Spent']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)
print(x_train.shape[0])
print(x_test.shape[0])
print(y_train.shape[0])
print(y_test.shape[0])

lm = LinearRegression()
lm.fit(x_train,y_train)
print(lm.coef_)
print(lm.intercept_)
predict = lm.predict(x_test)

plt.scatter(y=predict, x=y_test)
plt.show()

print("MAE: ", metrics.mean_absolute_error(y_test, predict))
print("MSE: ", metrics.mean_squared_error(y_test, predict))
print("RMSE: ", np.sqrt(metrics.mean_squared_error(y_test, predict)))

sns.distplot(y_test-predict)
plt.show()


coefs = pd.DataFrame(lm.coef_, x.columns, ['Coefs'])
print(coefs)
