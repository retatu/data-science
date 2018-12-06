import numpy as np
array = np.arange(0,30,3)
print(array)
#Elemento do indice 2
print(array[2])
#Todos elementos do indice 2 até o 5
print(array[2:5])
#Todos elemento até o indice 5
print(array[:5])
#TOdos elementos a partir do indice 2
print(array[2:])
#Alterar todos os elementos a partir do indice 5 para o valor 50
array[5:] = 50
print(array)

array = np.arange(50).reshape((5,10))
print(array)
array2 = array[:3]
print(array2)
#Altera os valores de ambos os arrays. TOdas alterações feitas do array2 irão para o array
#Para que isso nao aconteça deve ser utilizado oo método .copy()
array2[:] = 100
print(array)
print(array2)
array2 = array.copy()
array2[:] = 50
print("Utiizando o copy")
print(array)
print(array2)
#Vai buscar da posição 1 até a 4 nas linhas e as colunas a partir da coluna 3
#É separado por vírgula
print(array[1:4,3:])

#Retorna um array de booleano contendo cada true onde a posição é maior que 50
print(array > 50)

array = np.random.randint(20, size=50).reshape(5,10)
print(array)
posicoes_maiores_10 = array > 10
print(posicoes_maiores_10)
#Retorna um array contendo só as posições que foram True.
print(array[posicoes_maiores_10])

print(array[0:2, 3])
