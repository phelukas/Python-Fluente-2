import collections

# Criando uma tupla nomeada 'Carta', com os campos 'valor' e 'naipe'.
Carta = collections.namedtuple("Carta", ["valor", "naipe"])


class BaralhoFrances:
    # Cria uma lista dos valores das cartas, de 2 a 10, mais os 'J', 'Q', 'K', 'A'.
    valores = [str(n) for n in range(2, 11)] + list("JQKA")
    # Cria uma lista dos naipes das cartas. "spades" é paus, "diamonds" é ouros,
    # "clubs" é copas (corrigido de "clkubs"), e "hearts" é espadas.
    naipes = "paus ouros copas espadas".split()

    def __init__(self) -> None:
        # Cria a lista '_cartas', combinando cada valor com cada naipe.
        self._cartas = [
            Carta(valor, naipe) for naipe in self.naipes for valor in self.valores
        ]

    def __len__(self):
        # Retorna o número total de cartas no baralho.
        return len(self._cartas)

    def __getitem__(self, posicao):
        # Permite acessar uma carta específica do baralho usando a notação de índice, como em baralho[0].
        return self._cartas[posicao]


# Atribui um valor numérico a cada naipe para definir sua ordem de importância.
valores_naipes = dict(paus=3, copas=2, ouros=1, espadas=0)


def valor_com_paus_alto(carta):
    # Encontra o índice (posição) do valor da carta na lista de valores definida na classe BaralhoFrances.
    # Por exemplo, se a carta for um Ás, 'rank_value' pode ser 12, considerando que 'Ás' é o último valor na lista de 'valores'.
    valor_rank = BaralhoFrances.valores.index(carta.valor)

    # Calcula o valor total da carta, combinando seu valor com o valor do naipe para garantir
    # que as cartas sejam ordenadas primeiro por naipe e depois por seu valor.
    # Multiplica o índice do valor da carta pelo número total de naipes para criar um intervalo de valores
    # distintos para cada valor de carta dentro de cada naipe, e depois adiciona o valor do naipe específico da carta.
    return valor_rank * len(valores_naipes) + valores_naipes[carta.naipe]

baralho = BaralhoFrances()

for carta in sorted(baralho, key=valor_com_paus_alto):
    print(carta)
