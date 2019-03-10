import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

columns = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=columns)
movies_title = pd.read_csv('Movie_Id_Titles')
print(df.head())
print(df.info())

print(movies_title.head())
print(movies_title.info())

df = pd.merge(df, movies_title, on='item_id')
print(df.head())

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['count'] = pd.DataFrame(df.groupby('title')['rating'].count())
print(ratings.head())

ratings['count'].hist(bins=50)
plt.show()
ratings['rating'].hist(bins=50)
plt.show()

sns.jointplot(x='rating', y='count', data=ratings, alpha=0.5)
plt.show()

moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

#Pegando as avaliações de cada um dos filmes
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

#Similariedade das notas que as pessoas deram para esses filmes e starwars
similar_to_starwars = pd.DataFrame(moviemat.corrwith(starwars_user_ratings), columns=['Correlation'])
similar_to_starwars.dropna(inplace=True)
similar_to_starwars = similar_to_starwars.join(ratings['count'])
print(similar_to_starwars[similar_to_starwars['count']>75].sort_values('Correlation', ascending=False).head(10))

similar_to_liarliar = pd.DataFrame(moviemat.corrwith(liarliar_user_ratings), columns=['Correlation'])
similar_to_liarliar.dropna(inplace=True)
similar_to_liarliar = similar_to_liarliar.join(ratings['count'])
print(similar_to_liarliar[similar_to_liarliar['count'] > 75].sort_values('Correlation', ascending=False).head(10))












