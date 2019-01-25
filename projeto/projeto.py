import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')
print(df.info())
print(df.head())
#Top 5 ceps
print(df['zip'].value_counts().head(5))
#Top 5 cidades
print(df['twp'].value_counts().head(5))
#Titulos exclusivos que existem, pode ser usado o nunique tbm
print(df['title'].value_counts().count())
#Criar a coluna Razão no df
df['Reason'] = df['title'].apply(lambda x : x.split(':')[0])
print(df['Reason'])
#Motivo mais comum
print(df['Reason'].value_counts())
#Gerar gráfico de count plot das rasões
sns.countplot(data=df, x='Reason')
plt.show()
#Tipo de dado da coluna timestamp
print(type(df['timeStamp'][0]))
#Converter para timestamp
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
print(type(df['timeStamp'][0]))
#print(df['timeStamp'][0].hour)
#Criar colunas hora mes e dia da semana a partir da coluna timestamp
df['Hour'] = df['timeStamp'].apply(lambda x : x.hour)
df['Month'] = df['timeStamp'].apply(lambda x : x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x : x.dayofweek)
df['Day of Week'] = df['Day of Week'].map({0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'})
print(df['Day of Week'])

sns.countplot(x='Day of Week', data=df, hue='Reason')
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
plt.show()

sns.countplot(x='Month', data=df, hue='Reason')
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
plt.show()

#Criar dataframe e agrupar por mes, e utilizar o método count
byMonth = df.groupby('Month').count()
print(byMonth)

byMonth['twp'].plot()
plt.show()

sns.lmplot(x='Month',y='twp', data=byMonth.reset_index())
plt.show()

df['Date'] = df['timeStamp'].apply(lambda x : x.date())
print(df['Date'])


byDate = df.groupby('Date').count()
byDate['twp'].plot()
plt.show()

df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.show()

df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.show()

df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.show()

dia_hora = df.groupby(by=['Day of Week', 'Hour']).count()['twp'].unstack()
print(dia_hora)
sns.heatmap(dia_hora)
plt.show()

sns.clustermap(dia_hora)
plt.show()

dia_mes = df.groupby(by=['Day of Week', 'Month']).count()['twp'].unstack()
sns.heatmap(dia_mes)
plt.show()

sns.clustermap(dia_mes)
plt.show()