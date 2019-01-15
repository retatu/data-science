import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')

grid = sns.PairGrid(iris)

#O map vai aplicar a função para todos as relações possíveis
#replica o que o pairplot faz
#Cria os graficos de disperção com todas as variaveis correlacionadas com as outras
grid.map(plt.scatter)
plt.show()

#Ele aplicará o histograma para a digonal, scatter para os acima da diagonal e kdeplot para os abaixo
grid = sns.PairGrid(iris)
grid.map_diag(plt.hist)
grid.map_upper(plt.scatter)
grid.map_lower(sns.kdeplot)
plt.show()

sns.pairplot(iris, hue='species')
plt.show()

#Para trabalhar com dados categoricos
grid = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
grid.map(plt.hist, 'total_bill')
plt.show()