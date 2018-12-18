import numpy as np
import pandas as pd

labels = ['a','b','c']
lista = [10,20,10]
array = np.array(lista)
series = pd.Series(data=lista, index=labels)
print(series)
print("label 'b' da series:", series['b'])
#Utiizando o array
series = pd.Series(data=array, index=labels)
print(series)
#Pode até colocar metodos dentro de uma series
series = pd.Series([sum, print, len])
print(series)
serie1 = pd.Series([1,2,3,4], index=['EUA', 'Alemanha', 'Brasil', 'Argentina']);
print(serie1)
serie2 = pd.Series([1,2,3,4], index=['Alemanha', 'Brasil', 'EUA', 'Itália']);
print(serie2)
#Soma os valores de acirdo com o index, por exemplo: vai somar o valor da serie 1 com a chave EUA com o valor da serie 2 que tenha a mesma chave
serie3 = serie1+serie2
print(serie3)
