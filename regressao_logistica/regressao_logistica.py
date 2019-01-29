import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('titanic_train.csv')
print(train.head())
print(train.info())

plt.figure(figsize=(12,6))
#Mapa para verificar os dados nulos.
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()

sns.set_style('whitegrid')
#Plot dos passageiros que sobreviveram
sns.countplot(x='Survived', data=train, hue='Sex', palette='RdBu_r')
plt.show()
#Plot dos passageiros que sobreviveram por classe
sns.countplot(x='Survived', data=train, hue='Pclass', palette='rainbow')
plt.show()
#Idade
train['Age'].hist(bins=30, color='darkred', alpha=0.6)
plt.show()
#Acompanhantes
sns.countplot(x='SibSp', data=train)
plt.show()
#Idade das pessoas que não tiveram acompanhantes
train[train['SibSp']==0]['Age'].hist(bins=30)
plt.show()
train['Fare'].hist(bins=55, color='cyan')
plt.show()
train[train['Fare']<70]['Fare'].hist(bins=55, color='cyan')
plt.show()
