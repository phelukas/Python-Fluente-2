# Manipulação de arrays e operações com arquivos binários
from array import array
from random import random

# Criação de um array de floats com 10 milhões de números aleatórios
floats = array("d", (random() for i in range(10**7)))
print(floats[-1])  # Exibe o último valor gerado

# Salvando o array em um arquivo binário
with open("floats.bin", "wb") as fp:
    floats.tofile(fp)

# Lendo o array de volta do arquivo binário
floats2 = array("d")
with open("floats.bin", "rb") as fp:
    floats2.fromfile(fp, 10**7)

print(floats2[-1])  # Exibe o último valor lido
print(floats2 == floats)  # Verifica se os arrays são iguais (True)

# Uso de memoryview e cast de arrays
octets = array("B", range(6))
m1 = memoryview(octets)
print(m1.tolist())  # Exibe o array original

# Redimensionando a visualização com o cast
m2 = m1.cast("B", [2, 3])
print(m2.tolist())  # Exibe o array como 2x3

m3 = m1.cast("B", [3, 2])
print(m3.tolist())  # Exibe o array como 3x2

# Modificando valores via memoryview
m2[1, 1] = 22
m3[1, 1] = 33
print(octets)  # Exibe o array modificado: array('B', [0, 1, 2, 33, 22, 5])

# Manipulando arrays com memoryview e modificações diretas
numbers = array("h", [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))  # Exibe o comprimento do array
print(memv[0])  # Exibe o primeiro elemento (-2)

memv_oct = memv.cast("B")
print(memv_oct.tolist())  # Exibe o array em bytes

memv_oct[5] = 4
print(numbers)  # Exibe o array modificado: array('h', [-2, -1, 1024, 1, 2])

# Operações com NumPy
import numpy as np

a = np.arange(12)
print(a)  # Exibe o array 1D
print(a.shape)  # Exibe a forma do array

# Alterando a forma do array
a.shape = 3, 4
print(a)  # Exibe o array 3x4

# Acessando elementos
print(a[2])  # Exibe a terceira linha
print(a[2, 1])  # Exibe o elemento na terceira linha, segunda coluna
print(a[:, 1])  # Exibe a segunda coluna
print(a.transpose())  # Exibe o array transposto

# Carregando e salvando arrays com NumPy
floats = np.loadtxt("floats-10M-lines.txt")
print(floats[-3:])  # Exibe os últimos três elementos
floats *= 0.5
print(floats[-3:])  # Exibe os últimos três elementos após multiplicação

from time import perf_counter as pc

t0 = pc()
floats /= 3
print(pc() - t0)  # Exibe o tempo de execução

# Salvando e carregando arrays em formato binário
np.save("floats-10M", floats)
floats2 = np.load("floats-10M.npy", "r+")
floats2 *= 6
print(floats2[-3:])  # Exibe os últimos três elementos após multiplicação

# Uso de deque (fila de dois lados) para manipulação de sequências
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)  # Exibe o deque original

dq.rotate(3)  # Rotaciona para a direita
print(dq)  # Exibe o deque após a rotação

dq.rotate(-4)  # Rotaciona para a esquerda
print(dq)  # Exibe o deque após a rotação

# Adicionando elementos à esquerda e à direita
dq.appendleft(-1)
print(dq)  # Exibe o deque após inserir à esquerda

dq.extend([11, 22, 33])
print(dq)  # Exibe o deque após inserir à direita

dq.extendleft([10, 20, 30, 40])
print(dq)  # Exibe o deque após inserir à esquerda
