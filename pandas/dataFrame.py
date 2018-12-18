import numpy as np
import pandas as pd

np.random.seed(101)
#cria o data frame, index é as linhas e columns as colunas
dataFrame = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns ='W X Y Z'.split())
print(dataFrame)
print(type(dataFrame))
#Cada coluna é uma serie
print(type(dataFrame['W']))
print(dataFrame[['W', 'X']])
#Busca na coluna X na linha A
print(dataFrame['X']['A'])
dataFrame['novaColuna'] = dataFrame['W']+dataFrame['X']
print(dataFrame)
#Dropa a coluna, axis = 1 pq por default é 0(linha), inplace altera o valor do objeto, sem recisar atribuir o retorno a novo objeto
dataFrame.drop('novaColuna', axis=1, inplace=True)
print(dataFrame)
#Pega a LINHA
print(dataFrame.loc['A'])
#Linhas mais Colunas
print(dataFrame.loc[['A','B'], ['X','Z']])
#Fatiamento... primeiro a linha, passando as posiões e não o nome dos indexes
print(dataFrame.iloc[1:3, 1:])
