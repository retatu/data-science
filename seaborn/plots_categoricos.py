import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


#Cores default do seaborn
sns.set()

tips = sns.load_dataset('tips')

#gera um gráfico de barras da média do total_bill distinguido por sexo. O risco preto é o desvio padrão
sns.barplot(x='sex', y='total_bill', data=tips)
plt.show();

#com o estimator pode passar a própria função para plotagem dos gráficos, neste casso estou passando o desv pad.
#o desvio padrão gerado no gráfico(linha preta) será o desvio do desvio dos dados
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
plt.show();

#faz um gráfico da contagem dos valores
sns.countplot(x='sex', data=tips)
plt.show()

#Gera o gráfico dos quartis
sns.boxplot(x='day', y='total_bill', data=tips, hue='sex')
plt.show()
#Pega todos os dados não categoricos e gera o gráfico. o parâmetro H representa horizontal
sns.boxplot(data=tips, orient='h')
plt.show()

#Cria distribuição baseadas num modelo não paramétrico
#Split é utilizando quando os dados da esquerda são iguais aos dados da direita, então ele vai remover um e utilizar
#cada lada para um valor do hue
sns.violinplot(x='day', y='tip', data=tips, hue='sex', split=True)
plt.show()

#Gera o gráfico com todas as contágens
#o parâmetro jitter coloca os dados do lado, para ser mais fácil a visualização
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', dodge=True)
plt.show()

#Parecido com o stripplot mas é mais detalhado..
sns.swarmplot(x='day', y='total_bill', data=tips)
plt.show()

#Combinando dois gráficos
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
sns.violinplot(x='day', y='total_bill', data=tips)
plt.show()

#gera os outros gráficos de acordo com o tipo passado no parâmetro.
sns.catplot(x='day', y='total_bill', data=tips, kind='swarm')
plt.show()
