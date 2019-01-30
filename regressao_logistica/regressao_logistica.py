import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('titanic_train.csv')
print(train.head())
print(train.info())

plt.figure(figsize=(12,6))
#Mapa para verificar os dados nulos.
#sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
#plt.show()

sns.set_style('whitegrid')
#Plot dos passageiros que sobreviveram
#sns.countplot(x='Survived', data=train, hue='Sex', palette='RdBu_r')
#plt.show()
#Plot dos passageiros que sobreviveram por classe
#sns.countplot(x='Survived', data=train, hue='Pclass', palette='rainbow')
#plt.show()
#Idade
#train['Age'].hist(bins=30, color='darkred', alpha=0.6)
#plt.show()
#Acompanhantes
#sns.countplot(x='SibSp', data=train)
#plt.show()
#Idade das pessoas que não tiveram acompanhantes
#train[train['SibSp']==0]['Age'].hist(bins=30)
#plt.show()
#train['Fare'].hist(bins=55, color='cyan')
#plt.show()
#train[train['Fare']<70]['Fare'].hist(bins=55, color='cyan')
#plt.show()

#plt.figure(figsize=(12,6))
#Distribuição de idades por classe
#sns.boxplot(y='Age', x='Pclass', data=train)
#plt.show()


def set_idade(cols):
    idade = cols[0]
    pclass = cols[1]
    if pd.isnull(idade):
        if pclass == 1:
            return 37
        if pclass == 2:
            return 29
        else:
            return 24
    else:
        return idade

train['Age'] = train[['Age', 'Pclass']].apply(set_idade, axis=1)
#Não tem como preencher estes dados
del train['Cabin']
#Vai apagar a linha que possuir dados nulos
train.dropna(inplace=True)
#Mapa para verificar os dados nulos.
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()

#Tirar as variaveis categóricas para passar a ter categorias especificados por número
sex = pd.get_dummies(train['Sex'], drop_first=True)
embarked= pd.get_dummies(train['Embarked'], drop_first=True)
print(sex)
print(embarked)

train.drop(['Sex','PassengerId','Name','Ticket'], axis=1, inplace=True)
print(train)

train = pd.concat([train, sex, embarked], axis=1)
print(train.head())
