import numpy as np
lista = [1,2,3]
#converte em array numpy
print("Array: cria um array numpy")
print(np.array(lista))
matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(np.array(matriz))

print("Arange: gera uma sequencia de números em uma lista")
print(np.arange(0,10))
#intervalo de 2
print(np.arange(1,10,2))

print("Zeros: Preenche um array com zero")
print(np.zeros(5))
#array 2x3, precisa passar uma tupla
print(np.zeros((2,3)))

print("Ones: Preenche um array com um")
print(np.ones(5))
#array 2x3
print(np.ones((2,3)))

print("Eye: Cria matriz identidade")
print(np.eye(3))

print("Linspace: Cria um array e o terceiro parâmetro diz quantos número terão, ele faz o intervalo automaticamente")
print(np.linspace(0,10,3))
print(np.linspace(0,15,3))

print("Random: subbiblioteca.")
print("Random.rand: Cria um array de um intervalo randomico de 0 á 1")
print(np.random.rand(5))
print(np.random.rand(5)*10)
#para criar multidimencional não precisa passar uma tupla
print(np.random.rand(2,2))
print(np.random.rand(2,2,2))

print("Random.randn: Cria um array de um intervalo randomico, mas não são de uma distribuição unifome, mas de uma distribuição normal de média 0 e desv 1")
print(np.random.randn(5))
print(np.random.randn(5)*10)
print(np.random.randn(2,2))
print(np.random.randn(2,2,2))

print("Random.randit: Cria uma array de um intervalo especificado retirado de uma distribuição aleatoria, valores inteiro")
print(np.random.randint(5,100,5))

print("Array de valores inteiros de uma outra forma:")
print(np.round(np.random.rand(3,3)*100,0))


array = np.random.rand(25)
print(array)
print("reshape: muda a forma do array, as dimensões.")
reshape = array.reshape((5,5))
print(reshape)
print("Shape array: ",array.shape)
print("Shape array reshape: ",reshape.shape)

print("Maior valor e menor valor dentro de um array: Max e Min")
print("Maior reshape: ",reshape.max())
print("Menor reshape: ",reshape.min())

print("argmax e argmin: Reprenseta o indice do maior e menor valor no vetor")
print("Maior reshape", reshape.argmax())
print("Menor reshape", reshape.argmin())







