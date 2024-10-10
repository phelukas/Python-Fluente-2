# Importa o módulo namedtuple da coleção padrão
from collections import namedtuple

# (1) Definindo uma tupla nomeada chamada 'City', com os campos: nome, país, população, e coordenadas
City = namedtuple("City", "name country population coordinates")

# (2) Criando uma instância da tupla nomeada 'City' para a cidade de Tóquio
tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))

# Exibindo a instância 'tokyo'
# A saída será: City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(tokyo)

# (3) Acessando um campo específico da tupla nomeada por nome: 'population' (população)
# A saída será: 36.933
print(tokyo.population)

# Acessando um campo específico da tupla nomeada por nome: 'coordinates' (coordenadas)
# A saída será: (35.689722, 139.691667)
print(tokyo.coordinates)

# Acessando um campo específico da tupla nomeada por índice, no caso o índice 1 (país)
# A saída será: 'JP'
print(tokyo[1])

# Explicação:
# - É necessário fornecer dois parâmetros para criar uma tupla nomeada: um nome de classe ('City') e uma lista de campos ('name', 'country', etc.)
# - Os valores dos campos são passados como argumentos separados durante a criação de instâncias.
# - Campos podem ser acessados por nome (ex.: 'tokyo.population') ou por posição (ex.: 'tokyo[1]').

# (1) Exibindo os nomes dos campos da tupla nomeada usando a propriedade _fields
# A saída será: ('name', 'country', 'population', 'coordinates')
print(City._fields)

# Criando uma nova tupla nomeada 'Coordinate' para representar as coordenadas (latitude e longitude)
Coordinate = namedtuple("Coordinate", "lat lon")

# Criando uma lista de dados sobre Delhi NCR para construir uma nova instância de 'City'
delhi_data = ("Delhi NCR", "IN", 21.935, Coordinate(28.613889, 77.208889))

# (2) Criando uma nova instância de 'City' para Delhi NCR usando o método _make()
# _make() cria a instância de 'City' a partir de um iterável, como se fosse uma função de fábrica
delhi = City._make(delhi_data)

# (3) Convertendo a instância 'delhi' em um dicionário usando o método _asdict()
# _asdict() retorna um dicionário com os campos e valores correspondentes da instância
# A saída será: {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': Coordinate(lat=28.613889, lon=77.208889)}
print(delhi._asdict())

# (4) Convertendo o dicionário retornado por _asdict() para uma string JSON
# Isso é útil para serialização de dados, por exemplo, para enviar pela web
# A saída será: '{"name": "Delhi NCR", "country": "IN", "population": 21.935, "location": {"lat": 28.613889, "lon": 77.208889}}'
import json

print(json.dumps(delhi._asdict()))

# Explicações adicionais:
# - ._fields: Retorna uma tupla com os nomes dos campos da classe.
# - ._make(): Cria uma instância da tupla nomeada a partir de um iterável, como uma lista ou tupla.
# - ._asdict(): Converte a instância da tupla nomeada em um dicionário, associando cada campo ao seu valor.
# - ._asdict() é útil para converter a tupla nomeada em um formato que pode ser serializado, como JSON.
