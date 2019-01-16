import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')


df1 = pd.read_csv("df1", index_col=0)
df2 = pd.read_csv("df2")

print(df2)


#Plota a coluna A do df
df1['A'].hist()
plt.show()

#Plota todas as colunas
df2.plot.area(alpha=0.4)
plt.show()

#Com o parâmetro stacked=True juntaria tudo na mesma barra
df2.plot.bar()
plt.show()

print(df1.index)

df1.plot.line(y='B', use_index=True, figsize=(12,5), lw=1)
plt.show()

#O parâmetro C é reponsável por alterar a cor de acordo com o valor passado
df1.plot.scatter(x='A', y='B', c='C', cmap='inferno')
plt.show()

#Já o parâmetro S é reponsável por alterar o tamanho de acordo com o valor passado
df1.plot.scatter(x='A', y='B', s=df1['C']*20)
plt.show()

#Cria o boxplot
df2.plot.box()
plt.show()

df = pd.DataFrame(np.random.rand(1000,2 ), columns=['A','B'])
#Cria o mapa de calor
df.plot.hexbin(x='A',y='B',gridsize=10, cmap='inferno')
plt.show()

df2.plot.kde()
plt.show()