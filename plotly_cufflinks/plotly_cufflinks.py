import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cufflinks as cf
import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=False)
cf.go_offline()

df1 = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())
print(df1)

df2 = pd.DataFrame({'Categoria':['A','B','C'], 'Valores':[32,42,50]})
print(df2)

#Plota o scatter mas em formato de linhas
df1.iplot(kind='scatter', x='A', y='B')

#Em formato de pontos
df1.iplot(kind='scatter', x='A', y='B', mode='markers')

#Plota no estilo de barras
df2.iplot(kind='bar', x='Valores', y='Categoria')

#Plota odf1 em barras mas fica muito estranho
df1.iplot(kind='bar')

#Plota o df em gráfico de boxplot
df1.iplot(kind='box')

df3 = pd.DataFrame({'A':[1,2,3,4,5], 'B':[10,20,30,40,50], 'C':[5,4,3,2,1]})
#Plota em 3D
df3.iplot(kind='surface')

#Plota o gráfico em cima normal de linhas e em baixo gera a diferença entre eles
#df1[['A','B']].iplot(kind='spread')

#Gera o gráfico normal de histograma
df1['A'].iplot(kind='hist', bins=50)

#Gera um gráfico de bolha de A e B onde o tamanho é emfunção da variável C
df1.iplot(kind='bubble', x='A', y='B', size='C')
plt.show()

#Plota o gráfico no estilo do pairplot
df1.scatter_matrix()