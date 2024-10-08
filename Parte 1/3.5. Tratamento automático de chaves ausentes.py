class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0({1: "um", 2: "dois"})

# Procura a chave 1 (inteiro)
print(d[1])  # Saída: 'um'

# Procura a chave '1' (string)
print(d["1"])  # Saída: 'um'

# Procura uma chave que não existe
print(d[3])  # Levanta KeyError

d = StrKeyDict0({1: "um", 2: "dois"})

# Busca a chave 2 (inteiro)
print(d.get(2))  # Saída: 'dois'

# Busca a chave '2' (string)
print(d.get("2"))  # Saída: 'dois'

# Busca uma chave inexistente
print(d.get(3, "não encontrado"))  # Saída: 'não encontrado'

d = StrKeyDict0({1: "um", 2: "dois"})

print(1 in d)  # Saída: True (1 convertido para '1')
print("1" in d)  # Saída: True
print(3 in d)  # Saída: False
