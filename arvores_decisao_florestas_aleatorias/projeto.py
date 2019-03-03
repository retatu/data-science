import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv('loan_data.csv')
print(df.info())
print(df.head())

#Verificar se existe separação dos dados
#sns.pairplot(df, hue='not.fully.paid', diag_kind='hist')
#plt.show()


#df[df['credit.policy']==1]['fico'].hist(color='blue', alpha=0.5, bins=30, label='Credit Policy = 1')
#df[df['credit.policy']==0]['fico'].hist(color='red', alpha=0.5, bins=30, label='Credit Policy = 0')
#plt.legend()
#plt.show()

#df[df['not.fully.paid']==1]['fico'].hist(color='blue', alpha=0.5, bins=30, label='Not Fully Paid = 1')
#df[df['not.fully.paid']==0]['fico'].hist(color='red', alpha=0.5, bins=30, label='Not Fully Paid = 0')
#plt.legend()
#plt.show()

#plt.figure(figsize=(12,8))
#sns.countplot(x='purpose', data=df, hue='not.fully.paid')
#plt.show()

#sns.jointplot(x='fico', y='int.rate', data=df)
#plt.show()

#plt.figure(figsize=(12,6))
#sns.lmplot(x='fico',y='int.rate',data=df, hue='credit.policy', col='not.fully.paid')
#plt.show()

cat_feats = ['purpose']
final_df = pd.get_dummies(df, columns=cat_feats, drop_first=True)
print(final_df.info())


x_train, x_test, y_train, y_test = train_test_split(final_df.drop('not.fully.paid', axis=1), final_df['not.fully.paid'], test_size=0.3, random_state=101)
decision_tree = DecisionTreeClassifier()
decision_tree.fit(x_train, y_train)
predictions = decision_tree.predict(x_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))


random_forest = RandomForestClassifier(10)
random_forest.fit(x_train, y_train)
predictions = random_forest.predict(x_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))








