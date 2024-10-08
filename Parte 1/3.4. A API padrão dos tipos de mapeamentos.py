# Exemplos de tuplas com diferentes tipos de elementos

# Tupla contendo apenas elementos hashable (tupla dentro de uma tupla)
tt = (1, 2, (30, 40))
try:
    print(f"Hash de tt: {hash(tt)}")  # Isso funciona
except TypeError as e:
    print(f"Erro ao calcular hash de tt: {e}")

# Tupla contendo uma lista (não hashable)
tl = (1, 2, [30, 40])
try:
    print(f"Hash de tl: {hash(tl)}")  # Isso gera erro
except TypeError as e:
    print(f"Erro ao calcular hash de tl: {e}")

# Tupla contendo um frozenset (que é hashable)
tf = (1, 2, frozenset([30, 40]))
try:
    print(f"Hash de tf: {hash(tf)}")  # Isso funciona
except TypeError as e:
    print(f"Erro ao calcular hash de tf: {e}")
