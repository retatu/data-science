import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data, wb 
import datetime


BAC = data.DataReader ("BAC", "yahoo", datetime.datetime(2006, 1, 1), datetime.datetime(2016, 1, 1))
CB = data.DataReader ("CB", "yahoo", datetime.datetime(2006, 1, 1), datetime.datetime(2016, 1, 1))
GS = data.DataReader ("GS", "yahoo", datetime.datetime(2006, 1, 1), datetime.datetime(2016, 1, 1))
JPM = data.DataReader ("JPM", "yahoo", datetime.datetime(2006, 1, 1), datetime.datetime(2016, 1, 1))
MS = data.DataReader ("MS", "yahoo", datetime.datetime(2006, 1, 1), datetime.datetime(2016, 1, 1))
WFC = data.DataReader ("WFC", "yahoo", datetime.datetime(2006, 1, 1), datetime.datetime(2016, 1, 1))

tickers = ['BAC','CB','GS','JPM','MS','WFC']
#Coloca tudo em um df e adiciona os tickers como chave para cada um deles
bank_stocks = pd.concat(objs = [BAC, CB, GS, JPM, MS, WFC], axis=1, keys=tickers)
#Altera o nome das duas primeiras colunas 
bank_stocks.columns.names = ['Bank Ticker','Stock Info']
print(bank_stocks.head())
print(bank_stocks.info())
#Pega os maiores valores de fechamento de cada banco
print(bank_stocks.xs(key='Close', axis=1, level='Stock Info').max())
#Cria um novo df contendo os returns de cada banco
returns = pd.DataFrame()
for tick in tickers:
    returns[tick+' Returns'] = bank_stocks[tick]['Close'].pct_change()
print(returns.head())
sns.pairplot(returns[1:])
plt.show()

print(returns.idxmin(axis=0))
print(returns.idxmax(axis=0))

print(returns.std())
print(returns[returns.index.date > datetime.date(2015,1,1)].std())

sns.distplot(returns[(returns.index.date  >= datetime.date(2015,1,1)) & (returns.index.date  <= datetime.date(2015,12,31))]['MS Returns'], bins=50)
plt.show()

sns.distplot(returns[(returns.index.date  >= datetime.date(2008,1,1)) & (returns.index.date  <= datetime.date(2008,12,31))]['CB Returns'], bins=100)
plt.show()

bank_stocks.xs(key='Close', axis=1, level='Stock Info').plot(figsize=(12,3))
plt.show()

#Média movel é a média que varia de um determinado tempo, nesse caso, é feito a média sempre dos ultimos 30 dias
#Rolling faz agrupamento tipo o groupby mas a diferença é que passa um intervalo de linhas
media = bank_stocks.xs(key='Close', level='Stock Info', axis=1)['BAC'][bank_stocks.index.year == 2008].rolling(window=30).mean()
bank_stocks.xs(key='Close', level='Stock Info', axis=1)['BAC'][bank_stocks.index.year == 2008].plot(figsize=(12,5))
media.plot()
plt.show()

sns.heatmap(bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)
plt.show()

sns.clustermap(bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)
plt.show()