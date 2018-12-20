import numpy as np
import pandas as pd

np.random.seed(101)

d = {'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)
#Remove as colunas ou linas que possuem valores nulos
print(df.dropna())
#Vai excluir só os as colunas ou linha que tiverem '2' valores nulos
print(df.dropna(thresh=2))
#Altera as posições nulas por alguma coisa passada pelo parâmetro, nesse caso pela média dos valores na coluna
print(df.fillna(value=df.mean()))
#Preenche os valores com os dados anteriores
print(df.fillna(method='ffill'))
