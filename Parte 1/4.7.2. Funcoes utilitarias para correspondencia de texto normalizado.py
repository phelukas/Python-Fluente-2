"""
Funções utilitárias para comparação de strings Unicode normalizadas.

Usando a Normalização Forma C (NFC), sensível a maiúsculas/minúsculas:

    >>> s1 = 'café'
    >>> s2 = 'cafe\u0301'  # 'e' com acento combinante
    >>> s1 == s2
    False  # As strings parecem iguais, mas têm representações diferentes
    >>> nfc_equal(s1, s2)
    True  # Normalizando ambas as strings com NFC, elas se tornam iguais
    >>> nfc_equal('A', 'a')
    False  # A comparação é sensível a maiúsculas/minúsculas

Usando a Normalização Forma C com case folding (insensível a maiúsculas/minúsculas):

    >>> s3 = 'Straße'  # O caractere especial ß
    >>> s4 = 'strasse'  # Equivalente sem ß
    >>> s3 == s4
    False  # São diferentes visualmente
    >>> nfc_equal(s3, s4)
    False  # Mesmo normalizando com NFC, ainda são diferentes
    >>> fold_equal(s3, s4)
    True  # Com casefold, ß se transforma em "ss", tornando-as iguais
    >>> fold_equal(s1, s2)
    True  # Casefold e normalização tornam 'café' e 'cafe\u0301' iguais
    >>> fold_equal('A', 'a')
    True  # Casefold torna a comparação insensível a maiúsculas/minúsculas
"""

from unicodedata import normalize


def nfc_equal(str1, str2):
    """
    Compara duas strings usando a Normalização Forma C (NFC), sensível a
    maiúsculas/minúsculas.

    - NFC: Normalização que combina caracteres compostos e acentos combinantes
    em uma única forma "normalizada".

    Exemplo:
        - 'café' (com o caractere é precomposto) será igual a 'cafe\u0301'
        (onde 'e' e o acento agudo são separados), após normalização.

    :param str1: Primeira string.
    :param str2: Segunda string.
    :return: True se as strings forem iguais após a normalização NFC.
    """
    return normalize("NFC", str1) == normalize("NFC", str2)


def fold_equal(str1, str2):
    """
    Compara duas strings após aplicar a normalização NFC e o casefold, tornando
    a comparação insensível a maiúsculas/minúsculas.

    - Casefold: Um método mais agressivo que `lower()`, utilizado para tornar
    comparações insensíveis a caso, levando em consideração diferentes
    representações em diferentes línguas (como ß e µ).

    Exemplo:
        - 'Straße' será equivalente a 'strasse' após casefold, pois ß se torna 'ss'.
        - 'A' será equivalente a 'a' após casefold.

    :param str1: Primeira string.
    :param str2: Segunda string.
    :return: True se as strings forem iguais após normalização NFC e casefold.
    """
    return normalize("NFC", str1).casefold() == normalize("NFC", str2).casefold()

