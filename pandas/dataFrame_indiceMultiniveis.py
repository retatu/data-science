import numpy as np
import pandas as pd

outside = "G1 G1 G1 G2 G2 G2".split()
inside = [1,2,3,1,2,3]
#Cria uma lista de tuplas
hier_index = list(zip(outside,inside))
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
#Cria umdata frame com multi niveis, onde '1,2,3' serão subnivei de 'G1, G2'
df = pd.DataFrame(np.random.randn(6,2), index=hier_index, columns = ['A','B'])
print(df)
print(df.loc['G1'].loc[1]['A'])
#Define  nomes para os indexes
df.index.names = ['Grupo', 'Subgrupo']
print(df)
#Ao utilizar este no lugar do loc, pode passar direto o nivel mais interno, sem precisar acessar o mais externo primeiro
print(df.xs(2))
