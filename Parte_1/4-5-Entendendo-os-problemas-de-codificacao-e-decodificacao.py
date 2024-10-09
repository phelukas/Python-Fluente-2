# Define a string 'city' com o valor 'São Paulo'
city = "São Paulo"

# (1) Codifica a string 'city' em UTF-8. A codificação UTF-8 é uma das mais usadas e suporta caracteres especiais,
# como o "ã". A string é convertida para bytes, e o caractere 'ã' é representado pelos bytes \xc3\xa3.
city.encode("utf_8")
# Saída: b'S\xc3\xa3o Paulo'

# Codifica a string 'city' em UTF-16. Essa codificação usa 2 bytes para cada caractere,
# incluindo os espaços e letras, resultando em uma representação mais longa.
city.encode("utf_16")
# Saída: b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'

# (2) Codifica a string 'city' usando a codificação ISO-8859-1 (ou Latin-1), que suporta caracteres
# especiais como o "ã". Essa codificação é comum em idiomas europeus ocidentais.
city.encode("iso8859_1")
# Saída: b'S\xe3o Paulo'

# (3) Tenta codificar a string 'city' usando o conjunto de caracteres CP437, que era usado em sistemas MS-DOS.
# O CP437 não suporta o caractere 'ã', resultando em um UnicodeEncodeError.
city.encode("cp437")
# Erro: UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>

# (4) Codifica a string 'city' usando CP437, mas ignora os caracteres que não podem ser representados.
# O caractere 'ã' é ignorado, removendo-o da string.
city.encode("cp437", errors="ignore")
# Saída: b'So Paulo'

# (5) Codifica a string 'city' usando CP437, mas substitui os caracteres que não podem ser codificados por um
# caractere de substituição ("?"). O caractere 'ã' é substituído por "?".
city.encode("cp437", errors="replace")
# Saída: b'S?o Paulo'

# (6) Codifica a string 'city' usando CP437, mas substitui caracteres inválidos por suas referências
# numéricas XML. O caractere 'ã' é substituído por '&#227;', sua entidade em XML.
city.encode("cp437", errors="xmlcharrefreplace")
# Saída: b'S&#227;o Paulo'
