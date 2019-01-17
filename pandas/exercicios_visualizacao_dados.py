import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df3 = pd.read_csv('df3')

df3.plot.scatter(x='a', y='b', c='red', s=50, figsize=(12,3), linewidths=1, edgecolors='black')
plt.show()

df3['a'].plot.hist(color='blue', alpha=0.5)
plt.show()

df3['a'].plot.hist(bins=30,color='red', alpha=0.5, rwidth=2)
plt.show()

df3[['a','b']].plot.box()
plt.show()

df3['d'].plot.kde()
plt.show()

df3['d'].plot.kde(style='--', lw=5)
plt.show()

df3.loc[:30].plot.area(alpha=0.5)
plt.legend(loc='center left', bbox_to_anchor=(1.0,0.5))
plt.show()