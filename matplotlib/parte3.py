import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x*x

fig, ax = plt.subplots(figsize=(5,5))
#lINEWIDTH(ou lw) representa a grossura da linha
#Alpha seria uma especie de opacidade
#marker e markersize são parâmetros para definir um marcador e o seu tamanho
ax.plot(x,x**2,color='#2F3BBF',label='Titulo1', lw=3, alpha=0.3,
        linestyle='--',marker='s', markersize=10, markerfacecolor='black')
ax.plot(x,x**3,color='#FB12BB',label='Titulo1', linewidth=0.7, linestyle='--', marker='o')
ax.legend()
plt.show()

fig, ax = plt.subplots(figsize=(5,5))
ax.plot(x,x**2)
ax.plot(x,x**3)
#Lim altera até quais valores aparecerão no gráfico
ax.set_xlim([0,3])
ax.set_ylim([0,15])
plt.show()

#Coloca apenas os pontos
plt.scatter(x,y)
plt.show()

#Histogramas
plt.hist(y)
plt.show()

#BoxPlot
plt.boxplot([x,y],vert=True, patch_artist=True)
plt.show()
