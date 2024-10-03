# Operações de slicing com listas
l = [10, 20, 30, 40, 50, 60]
print(l[:2])  # split at 2, resultado: [10, 20]
print(l[2:])  # resultado: [30, 40, 50, 60]
print(l[:3])  # split at 3, resultado: [10, 20, 30]
print(l[3:])  # resultado: [40, 50, 60]

# Operações de slicing com strings
s = "bicycle"
print(s[::3])  # resultado: 'bye'
print(s[::-1])  # resultado: 'elcycib'
print(s[::-2])  # resultado: 'eccb'

# Processamento de uma fatura com slicing
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""

# Definição dos slices para diferentes partes da fatura
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

# Divisão das linhas da fatura e exibição dos dados relevantes
line_items = invoice.split("\n")[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# Alteração de listas com slicing
l = list(range(10))
print(l)  # resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Substituindo elementos da lista
l[2:5] = [20, 30]
print(l)  # resultado: [0, 1, 20, 30, 5, 6, 7, 8, 9]

# Deletando elementos da lista
del l[5:7]
print(l)  # resultado: [0, 1, 20, 30, 5, 8, 9]

# Atribuindo valores com slicing
l[3::2] = [11, 22]
print(l)  # resultado: [0, 1, 20, 11, 5, 22, 9]

# Tentativa de atribuição inválida
try:
    l[2:5] = 100  # Isso gera um erro, pois só pode atribuir iteráveis
except TypeError as e:
    print(e)

# Correção da atribuição
l[2:5] = [100]
print(l)  # resultado: [0, 1, 100, 22, 9]
