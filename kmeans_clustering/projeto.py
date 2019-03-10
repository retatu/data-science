import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

data = pd.read_csv('College_Data')
print(data.head())
print(data.info())

#private =pd.get_dummies(data['Private'], drop_first=True, prefix = 'Private')
#data.drop(['Private'], axis=1, inplace=True)
#data = pd.concat([data, private], axis=1)
#print(data.info())

sns.lmplot('Grad.Rate', 'Room.Board', data = data, hue='Private', fit_reg=False, palette='coolwarm')
plt.show()

sns.lmplot( 'Outstate', 'F.Undergrad', data = data, hue='Private', fit_reg=False, palette='coolwarm')
plt.show()

g = sns.FacetGrid(data, hue='Private')
g = g.map(plt.hist, 'Outstate', bins=30, alpha=0.7)
plt.show()

g = sns.FacetGrid(data, hue='Private')
g = g.map(plt.hist, 'Grad.Rate', bins=30, alpha=0.7)
plt.show()

print(data[data['Grad.Rate']>100])
data['Grad.Rate']['Cazenovia College'] = 100


kmc = KMeans(n_clusters=2)
kmc.fit(data.drop(['Private', 'Unnamed: 0'], inplace=False, axis=1))
print(kmc.cluster_centers_)

def yes_to_1(cluster):
    if cluster == 'Yes':
        return 1
    else:
        return 0

data['Cluster'] = data['Private'].apply(yes_to_1)
print(data.head())

print(classification_report(data['Cluster'], kmc.labels_))
print(confusion_matrix(data['Cluster'], kmc.labels_))
