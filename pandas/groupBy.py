import numpy as np
import pandas as pd

data = {'Empresa':['GOOG', 'GOOG','MSFT', 'MSFT', 'FB', 'FB'],
        'Nome':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sam'],
        'Venda':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)
#Agrupo pelo dipo de empresa
group = df.groupby('Empresa')
#Realiza a soma por empresa
print(group.sum())
#Média por empresa
print(group.mean())
#Várias informações
print(group.describe())
#A coluna do nome não é contada porque é de texto. Com o count vai mostrar
print(group.count())
print(group.sum().loc['GOOG'])
