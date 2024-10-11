# Definindo a classe Bus
class Bus:
    # Construtor da classe
    def __init__(self, passengers=None):
        # Se nenhum passageiro for fornecido, cria uma lista vazia
        if passengers is None:
            self.passengers = []
        else:
            # Faz uma cópia da lista de passageiros fornecida
            self.passengers = list(passengers)

    # Método para adicionar um passageiro
    def pick(self, name):
        self.passengers.append(name)

    # Método para remover um passageiro
    def drop(self, name):
        self.passengers.remove(name)


# Importando o módulo copy para trabalhar com cópias rasas e profundas
import copy

# Criando um objeto bus1 com alguns passageiros
bus1 = Bus(["Alice", "Bill", "Claire", "David"])

# Fazendo uma cópia rasa (shallow copy) do objeto bus1
bus2 = copy.copy(bus1)

# Fazendo uma cópia profunda (deep copy) do objeto bus1
bus3 = copy.deepcopy(bus1)

# Verificando os IDs dos objetos (1)
print(id(bus1), id(bus2), id(bus3))
# Resultado: (IDs diferentes, indicando que são objetos diferentes)

# Removendo um passageiro de bus1
bus1.drop("Bill")

# Verificando os passageiros em bus2 (2)
print(bus2.passengers)
# Resultado: ['Alice', 'Claire', 'David']
# A remoção de 'Bill' também afetou bus2, pois ambos compartilham a mesma lista de passageiros (cópia rasa)

# Verificando os IDs das listas de passageiros em cada objeto (3)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
# Resultado: (IDs iguais para bus1 e bus2, diferente para bus3)
# bus1 e bus2 compartilham a mesma lista de passageiros, enquanto bus3 tem sua própria cópia (cópia profunda)

# Verificando os passageiros em bus3 (4)
print(bus3.passengers)
# Resultado: ['Alice', 'Bill', 'Claire', 'David']
# A cópia profunda de bus1 mantém a lista de passageiros original, independente das mudanças em bus1 ou bus2

# Exemplo de referência cíclica
# Criando uma lista 'a' e uma lista 'b' que contém 'a'
a = [10, 20]
b = [a, 30]
# Adicionando 'b' como um elemento em 'a', criando uma referência cíclica
a.append(b)
print(a)
# Resultado: [10, 20, [[...], 30]]
# A lista 'a' contém uma referência para si própria, gerando uma referência cíclica

# Fazendo uma cópia profunda de 'a'
c = copy.deepcopy(a)
print(c)
# Resultado: [10, 20, [[...], 30]]
# A cópia profunda preserva a estrutura cíclica sem compartilhar referências com a lista original
