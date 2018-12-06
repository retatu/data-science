import numpy as np

array = np.arange(0,16)
#Faz a operação matemática de poição por posição, tem que ser do mesmo tamanho
print(array+array)
#Vai fazer a operação indice por indice
print(2**array)
#Faz a raiz quadrada de todo o array
print(np.sqrt(array))
#Exponeciação de torra array
print(np.exp(array))
#Média dos valores no array
print(np.mean(array))
#Desvio padrão dos valores no arrays
print(np.std(array))
#Seno, coseno e tangente do valores no array
print(np.sin(array))
print(np.cos(array))
print(np.tan(array))
#Menor valor
print(np.min(array))
