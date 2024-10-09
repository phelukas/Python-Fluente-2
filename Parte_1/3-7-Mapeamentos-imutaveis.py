# Importa o tipo MappingProxyType, que cria uma visão somente leitura de um dicionário
from types import MappingProxyType

# Cria um dicionário simples com um par chave-valor
d = {1: "A"}

# Cria uma "proxy" somente leitura do dicionário 'd' usando MappingProxyType
d_proxy = MappingProxyType(d)

# Exibe a proxy. A proxy reflete o estado atual do dicionário 'd', mostrando o conteúdo de 'd'
d_proxy  # Saída: mappingproxy({1: 'A'})

# Acessa o valor associado à chave 1 na proxy.
# Como a proxy é só leitura, podemos acessar valores sem problemas
d_proxy[1]  # Saída: 'A'

# Tenta atribuir um novo valor à chave 2 na proxy.
# Isso gera um erro porque a proxy é somente leitura e não permite modificações diretas
d_proxy[2] = (
    "x"  # Erro: TypeError: 'mappingproxy' object does not support item assignment
)

# Modifica diretamente o dicionário original 'd', adicionando um novo par chave-valor (2: 'B')
d[2] = "B"

# Exibe novamente a proxy.
# Observe que a proxy agora reflete as alterações feitas no dicionário original, mostrando o novo item (2: 'B')
d_proxy  # Saída: mappingproxy({1: 'A', 2: 'B'})

# Acessa o valor associado à chave 2 na proxy. Como a proxy reflete as mudanças no dicionário original,
# ela retorna o valor atualizado da chave 2, que foi adicionado ao dicionário 'd'
d_proxy[2]  # Saída: 'B'
