import typing
from dataclasses import dataclass


"""
Por que @dataclass é a melhor opção aqui?

Automação: Cria automaticamente o método __init__ com valores padrão para b e c, além de gerar __repr__ e `eq.
Flexível: Suporta mutabilidade e pode ser estendida para atender a necessidades mais complexas com menos esforço.
Leitura: O código é simples e limpo, tornando-o fácil de ler e manter.
"""


class DemoPlainClass:
    a: int
    b: float = 1.1
    c = "spam"


class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = "spam"


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = "spam"
