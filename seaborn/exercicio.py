import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.head())

sns.jointplot(x='fare', y='age', data=titanic)
plt.show()

sns.distplot(titanic['fare'], kde=False, color='red')
plt.show()

sns.boxplot(x='class', y='age', data=titanic)
plt.show()

sns.swarmplot(x='class', y='age', data=titanic)
plt.show()

sns.countplot(x='sex', data=titanic)
plt.show()

sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.title('titanic.corr')
plt.show()


grid = sns.FacetGrid(titanic, col='sex')
grid.map(plt.hist, 'age')
plt.show()
