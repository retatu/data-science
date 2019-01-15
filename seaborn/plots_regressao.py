import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set()

tips = sns.load_dataset('tips')

#Cria o plot de linear module
#Cria uma regrassão linear entre o total da conta e a gorjeta
#Utilizando o scatter_kws da para alterar os valores do scatter plot passando um dicionado como parâmetro
#onde a chave vai ser o parâmetro e o valor o valor do parâmetro
#o col divide os valores entre os tipos. No caso, será entre sexo
#o row faz a mesma coisa que o col, mas em vez de dividir em colunas divide em linhas
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o','v'], scatter_kws={'s':100}, col='sex', row='time')
plt.show()

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='day')
plt.show()
