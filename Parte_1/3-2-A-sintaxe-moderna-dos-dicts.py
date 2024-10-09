dial_codes = [
    (880, "Bangladesh"),
    (55, "Brasil"),
    (86, "China"),
    (91, "Índia"),
    (62, "Indonésia"),
    (81, "Japão"),
    (234, "Nigéria"),
    (92, "Paquistão"),
    (7, "Rússia"),
    (1, "Estados Unidos"),
]

country_dial = {country: code for code, country in dial_codes}

{code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}

# d1 | d2: cria um novo dicionário, combinando os dois dicionários, sem modificar d1.
# d1 |= d2: modifica o dicionário d1 atualizando-o com os valores de d2.

d1 = {"a": 1, "b": 3}
d2 = {"a": 2, "b": 4, "c": 6}
d1 | d2
{"a": 2, "b": 4, "c": 6}

{"a": 1, "b": 3}
d1 |= d2
{"a": 2, "b": 4, "c": 6}
