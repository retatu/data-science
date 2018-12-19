import numpy as np
import pandas as pd

np.random.seed(101)
#cria o data frame, index é as linhas e columns as colunas
dataFrame = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns ='W X Y Z'.split())
print(dataFrame)
print(type(dataFrame))
print(dataFrame>0)
maiores_que_zero = dataFrame>0
print(dataFrame[maiores_que_zero])
#Vai retornar somente as linhas que tiverem a COLUNA W maior que zero
print(dataFrame[dataFrame['W']>0])
#Retorna os valores da coluna Z onde os valores da coluna W são maiores que 0
print(dataFrame[dataFrame['W']>0]['Z'])
#utilizar | e & no lugar do "or" e "and"
print(dataFrame[(dataFrame['W']>0) & (dataFrame['Y']>0)])
print(dataFrame[(dataFrame['W']>0) | (dataFrame['Y']>0)])

#Altera o dataframe para resetar o index
print(dataFrame.reset_index(inplace=True))
col = "RS RJ SP AM SC".split()
dataFrame['Estado'] = col
print(dataFrame)
#Altera o index do data frama
dataFrame.set_index("Estado", inplace=True)
print(dataFrame)
