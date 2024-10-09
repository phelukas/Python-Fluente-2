"""
vector2d.py: uma classe simplista demonstrando alguns métodos especiais

É simplista por razões didáticas. Não possui um tratamento de erro adequado,
especialmente nos métodos ``__add__`` e ``__mul__``.

Adição::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

Valor absoluto::

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

Multiplicação escalar::

    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0

Diferença entre str() e repr():
    str(): Retorna uma representação amigável do objeto, destinada ao uso para o público (usuário final).
    repr(): Retorna uma representação mais técnica, usada para depuração, e que tenta ser o mais precisa possível.
    
"""

import math  # Importa o módulo math para usar funções matemáticas, como calcular a hipotenusa.

class Vector:

    def __init__(self, x=0, y=0):
        # Método construtor. Inicializa um vetor com coordenadas x e y. 
        # Se nenhum valor for passado, ele inicializa o vetor em (0, 0).
        self.x = x
        self.y = y

    def __repr__(self):
        # Método especial que retorna uma representação "oficial" do objeto.
        # Isso é útil, por exemplo, para exibir o vetor ao usar o print().
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        # Método especial que retorna o valor absoluto (magnitude) do vetor.
        # Usa a fórmula da hipotenusa para calcular: sqrt(x^2 + y^2).
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # Método especial que define como o objeto é avaliado em um contexto booleano.
        # Retorna False se o vetor for (0, 0) (magnitude 0), e True caso contrário.
        return bool(abs(self))

    def __add__(self, other):
        # Método especial que define o comportamento da adição entre dois vetores.
        # Soma as coordenadas x e y dos dois vetores e retorna um novo vetor.
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        # Método especial que define o comportamento da multiplicação escalar.
        # Multiplica as coordenadas x e y do vetor pelo escalar fornecido.
        return Vector(self.x * scalar, self.y * scalar)
