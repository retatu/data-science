import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':[np.nan,'def','ghi','xyz']})

#Retorna os valores sem repetir eles, pode ser feito usando numpy tbm
print(df['col2'].unique())
#Quantidade de valores distintos
print(df['col2'].nunique())
#Vai juntar os vaores repetidos
print(df['col2'].value_counts())
#Vai retornar só as linhas que tiverem valores na coluna 1 maior que 2 e na coluna 2 igual a 444
print(df[(df['col1']>2) & (df['col2']==444)])
#Vai somar ou concatenar os valores por colunas
print(df.sum())
print(df['col2'].sum())

def vezes2(x):
    return x*2
#Passa um método para ser aplicado pelos valores do df
print(df.apply(vezes2))
print(df.apply(len))
print(df['col1'].apply(lambda x : x*x))

#deletar colunas
del df['col1']
print(df)
print(df.columns)
print(df.index)
#Reordena as linhas de acordo com a coluna passada
print(df.sort_values('col2'))
#Mostra quais posições são nulas
print(df.isnull())
#Tira os nullos
print(df.dropna())
#PReenche os valores nulos comm o que é especificado
print(df.fillna('nulo'))


df = {'A':['foo','foo','foo','bar','bar','bar'],
      'B':['one','one','two','two','one','one'],
      'C':['x','y','x','y','x','y'],
      'D':[1,3,2,4,3,1]}
df=pd.DataFrame(df)
#Reordenaos dados com subtabelas, onde os valores serão os da coluna D, as colunas serãoos os valores da coluna C
#e os indexes serão da coluna A e B.
print(df.pivot_table(values='D', index=['A','B'], columns=['C']))










