import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set()

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())
print(flights.head())

#Cacula todas as correlações do ds
print(tips.corr())
print(flights.corr())

#Gera mapa de calor das correlações. annot mostra os valores dentro de cara 'caixinha"
sns.heatmap(tips.corr(), annot=True)
plt.show()
sns.heatmap(flights.corr(), annot=True)
plt.show()

#Reorganiza os dados com colunas linhas e valores
pf_flights = flights.pivot_table(values='passengers', index='month', columns='year')
sns.heatmap(pf_flights, linecolor='green', linewidths=1)
plt.show()

#Cria heat map com agrupamento dos dados que o algoritmo diz serem relevantes. Serve para encontrar padrões
#Standard scale altera o range. para ficar mais visivel os agrupamentos
sns.clustermap(pf_flights, standard_scale=1)
plt.show()