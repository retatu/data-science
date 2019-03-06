import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8, random_state=50)

plt.scatter(data[0][:, 0], data[0][:, 1], c=data[1], cmap = 'rainbow')
plt.show()
#Parâmetro é a quantidade de grupos. Sei que é 4 grupos por causa do gráfico de cima, onde existe 4 cores
kmeans = KMeans(n_clusters = 4)
kmeans.fit(data[0])
print(kmeans.labels_)


#Comparação dos dados reais e os dados do modelo
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12,8))
ax1.set_title('Dataset')
ax1.scatter(data[0][:, 0], data[0][:, 1], c=data[1], cmap = 'rainbow')
ax2.set_title('Kmeans')
ax2.scatter(data[0][:, 0], data[0][:, 1], c=kmeans.labels_, cmap = 'rainbow')
plt.show()
