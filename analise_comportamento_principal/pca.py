import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

cancer = load_breast_cancer()
print(cancer.keys())
print(cancer['target_names'])
print(cancer['DESCR'])
print(cancer['data'])

df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
print(df.head())
print(df.info())

#Normalização
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

#Transformar um conjunto de dados que tinha 30 dimensões em um conjunto com 2 dimensões
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)
print(x_pca.shape)
print(x_pca)

fig, ax = plt.subplots()
ax.scatter(x_pca[:, 0], x_pca[:, 1], c=cancer['target'])
plt.show()


df_comp = pd.DataFrame(pca.components_, columns=cancer['feature_names'])
sns.heatmap(df_comp)
plt.show()













