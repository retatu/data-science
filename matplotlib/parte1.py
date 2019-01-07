import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x*x

print(x)
print(y)

#Funcional
#O parâmetro 'r--' é da linha, nesse caso, seria tracejado.
plt.plot(x,y,'r--' ,color='g')
plt.xlabel('Leganda x')
plt.ylabel('Legenda y')
plt.title('Titulo')
plt.show()


#Para criar subgraficos
#Dois gráficos por linha. Terceiro parâmetro sinaliza qual dos gráficos será mexido
plt.subplot(1,2,1)
plt.plot(x,y,'r--')
#Mexendo no segundo gráfico agora
plt.subplot(1,2,2)
plt.plot(y,x,'g*-')
plt.show()


#Esse fig é tipo um panel que vai armazenar os gráficos
fig = plt.figure()
#Adiciona o axes1 na figura nas distâncias passadas pela lista
axes1 = fig.add_axes([0.1,0.1,0.7,0.7])
#Adicionado o axes2
axes2 = fig.add_axes([0.2,0.5,0.3,0.3])
axes1.plot(x,y,'r--')
axes2.plot(y,x,'g*-')
plt.show()
