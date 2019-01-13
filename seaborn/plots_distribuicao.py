import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


#Cores default do seaborn
sns.set()

tips = sns.load_dataset('tips')
print(tips)
#Gera um histograma com com a curva kde
#kde true é a para ativar/remover a curva, por default é true
#bins é o tamanho do agrupamento, é feito de forma automática, mas pode ser alterado
sns.distplot(tips['total_bill'],kde=True, bins=15)
plt.show()

#Gera uma curva da distribuição igual ao displot mas com duas variáveis ao mesmo tempo
#parâmetro kind faz regressao linear dos valores; o valor 'hex' no kind faz um mapa de calor
sns.jointplot(x=tips['total_bill'], y=tips['tip'], data=tips, kind='reg')
plt.show()

#Gera joinplots de todos os dados númericos
#parâmetro hue faz com que pinte diferente de acordo com a coluna passada
sns.pairplot(tips, hue='sex', kind = 'reg')
plt.show()

#Gera o kde
sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])
plt.show()