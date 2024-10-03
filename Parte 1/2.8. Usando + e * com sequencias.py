# Multiplicação de listas e strings
l = [1, 2, 3]
print(l * 5)  # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(5 * "abcd")  # 'abcdabcdabcdabcdabcd'

# Tabuleiro 3x3 com listas
board = [["_"] * 3 for i in range(3)]  # Criação de um tabuleiro com listas separadas
print(board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = "X"  # Modifica a posição [1][2]
print(board)  # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

# Atenção ao uso de listas aninhadas compartilhadas
weird_board = [["_"] * 3] * 3  # Criação de um tabuleiro com referências à mesma lista
print(weird_board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
weird_board[1][2] = "O"  # Modifica a posição [1][2], alterando todas as linhas
print(weird_board)  # [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]

# Cuidado ao adicionar a mesma linha a várias listas
row = ["_"] * 3
board = []
for i in range(3):
    board.append(row)  # Adiciona a mesma lista a cada linha

# Forma correta de criar listas aninhadas independentes
board = []
for i in range(3):
    row = ["_"] * 3  # Cria uma nova linha a cada iteração
    board.append(row)
print(board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[2][0] = "X"  # Modifica apenas a posição [2][0]
print(board)  # [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]

# Operações com listas e tuplas, verificando IDs
l = [1, 2, 3]
print(id(l))  # Exibe o ID da lista
l *= 2  # Multiplica a lista
print(l)  # [1, 2, 3, 1, 2, 3]
print(id(l))  # O ID permanece o mesmo, pois a lista é mutável

t = (1, 2, 3)
print(id(t))  # Exibe o ID da tupla
t *= 2  # Multiplica a tupla
print(id(t))  # O ID muda, pois tuplas são imutáveis

# Operações em tuplas com elementos mutáveis
t = (1, 2, [30, 40])
t[2] += [50, 60]  # Modificação ocorre na lista dentro da tupla, não na tupla em si
print(t)  # (1, 2, [30, 40, 50, 60])

# Erro ao tentar modificar tupla diretamente
t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]  # Lança erro de 'tuple' object does not support item assignment
except TypeError as e:
    print(e)
print(t)  # Apesar do erro, a lista foi modificada: (1, 2, [30, 40, 50, 60])
