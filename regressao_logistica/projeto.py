import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv('advertising.csv')
print(df.head())
print(df.info())

#plt.figure(figsize=(12,6))
#df['Age'].hist(bins=30, color='darkblue', alpha=0.6)
#plt.show()

#sns.jointplot(x='Age',y='Area Income',data=df)
#plt.show()

#sns.jointplot(x='Age',y='Daily Time Spent on Site',data=df, kind='kde')
#plt.show()

#sns.jointplot(x='Daily Time Spent on Site',y='Daily Internet Usage',data=df, color='green')
#plt.show()

sns.pairplot(df, hue='Clicked on Ad', palette='bwr', diag_kind='hist')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(df[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','Male']], df['Clicked on Ad'], test_size=0.3)

logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)
predictions = logmodel.predict(x_test)

print(classification_report(y_test, predictions))
