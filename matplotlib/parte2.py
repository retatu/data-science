import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x*x

#Subplot utiliza a orientação a objetos, para não precisar ficar especificando qual
#gráfico será editado nos parâmetros.
fig, ax = plt.subplots()
ax.plot(x, x**3, 'b--')
ax.plot(x, x**4, 'g-.')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Titulo')
plt.show()

#Cria sub gráficos
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(x,y, 'b-')
ax[0].set_title('grafico1')
ax[1].plot(x,y**2, 'b*')
ax[1].set_title('grafico2')
plt.show()


fig, axes = plt.subplots(figsize=(8,3))
axes.plot(x,y,'r',label='leganda1')
axes.plot(y,x,'g', label='legenda2')
axes.legend()
fig.savefig('img.png')
plt.show()

