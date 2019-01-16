import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

#Style altera o fundo do grádico
sns.set_style('darkgrid')
sns.countplot(x='sex', data=tips)
plt.show()
sns.set_style('whitegrid')
sns.countplot(x='sex', data=tips)
plt.show()
sns.set_style('ticks')
#Seaborn permite passar os métodos o plt para alterar os estilos
plt.figure(figsize=(12,4))
sns.countplot(x='sex', data=tips)
#Remove as bordas. por padrão fica da esquerda e a do bottom
sns.despine(left=True, top=False)
plt.show()

#Altera largura e altura do plto linear
sns.lmplot(x='total_bill', y='tip', data=tips, height=5, aspect=4)
plt.show()

sns.set_context('poster', font_scale=1.3)
sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()

#paletas disponiveis: https://matplotlib.org/examples/color/colormaps_reference.html
sns.set_context('notebook', font_scale=1)
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='inferno')
plt.show()