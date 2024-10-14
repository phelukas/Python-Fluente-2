Funções de ordem superior (Higher-Order Functions) são funções que **podem receber outras funções como argumentos e/ou retornar outras funções como resultado**. Em Python, as funções de ordem superior são bastante comuns e poderosas, permitindo uma abordagem funcional para resolver problemas. Essa capacidade de trabalhar com funções como qualquer outro tipo de dado torna o código mais flexível e expressivo.

### Exemplos de Funções de Ordem Superior

Aqui estão duas características principais de uma função de ordem superior:

1. **Receber uma Função como Argumento**: 
   Uma função que recebe outra função como argumento é uma função de ordem superior. Isso permite aplicar uma função a diferentes entradas sem modificar a lógica principal.

   Exemplos em Python incluem `map()`, `filter()` e `sorted()`, que usam outras funções para operar sobre listas ou iteráveis.

   ```python
   # Exemplo usando map
   def quadrado(x):
       return x * x

   numeros = [1, 2, 3, 4]
   resultado = map(quadrado, numeros)
   print(list(resultado))  # Saída: [1, 4, 9, 16]
   ```

   Nesse exemplo, `map()` é uma função de ordem superior, pois recebe a função `quadrado` como argumento e a aplica a cada elemento da lista `numeros`.

2. **Retornar uma Função como Resultado**:
   Uma função também é considerada de ordem superior se retorna outra função. Isso é útil quando queremos criar funções dinâmicas, gerando novas funções baseadas em entradas específicas.

   ```python
   def multiplicador(n):
       def multiplica_por(x):
           return x * n
       return multiplica_por

   # Cria uma função que multiplica por 3
   multiplica_por_3 = multiplicador(3)
   print(multiplica_por_3(10))  # Saída: 30
   ```

   No exemplo acima, `multiplicador` é uma função que retorna uma nova função, `multiplica_por`. Isso permite criar funções personalizadas com base nos argumentos fornecidos.

### Funções Integradas que são de Ordem Superior

Python possui várias funções embutidas que são funções de ordem superior, incluindo:

- **`map(function, iterable)`**: Aplica a `function` a cada item do `iterable` e retorna um mapa do resultado.
  
  ```python
  numeros = [1, 2, 3, 4]
  resultado = map(lambda x: x * 2, numeros)
  print(list(resultado))  # Saída: [2, 4, 6, 8]
  ```

- **`filter(function, iterable)`**: Retorna os elementos do `iterable` que satisfazem a condição definida na `function` (função que deve retornar `True` ou `False`).

  ```python
  numeros = [1, 2, 3, 4, 5, 6]
  pares = filter(lambda x: x % 2 == 0, numeros)
  print(list(pares))  # Saída: [2, 4, 6]
  ```

- **`reduce(function, iterable)`** (do módulo `functools`): Reduz um `iterable` a um único valor, aplicando a `function` de maneira cumulativa.

  ```python
  from functools import reduce

  numeros = [1, 2, 3, 4]
  soma = reduce(lambda x, y: x + y, numeros)
  print(soma)  # Saída: 10
  ```

### Quando Usar Funções de Ordem Superior

Funções de ordem superior são particularmente úteis quando:

- **Abstrair a Lógica**: Quando há uma operação comum que precisa ser aplicada a diferentes coleções de dados. Por exemplo, aplicar uma transformação a cada elemento de uma lista (como `map`).
- **Evitar Repetição de Código**: Elas ajudam a evitar código repetitivo, pois permitem que uma lógica comum seja abstraída em funções reutilizáveis.
- **Programação Funcional**: São uma base da programação funcional, que permite que funções sejam tratadas como "cidadãos de primeira classe" (podem ser passadas, retornadas, armazenadas, etc.).

### Exemplo Prático

Um exemplo típico de uso é combinar várias operações de filtragem e transformação em uma lista:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Filtra números pares e depois aplica o quadrado a cada um deles
pares_quadrados = map(lambda x: x * x, filter(lambda x: x % 2 == 0, numeros))
print(list(pares_quadrados))  # Saída: [4, 16, 36, 64]
```

Nesse exemplo, `filter()` filtra os números pares e `map()` aplica o quadrado em cada número. Ambos são funções de ordem superior que ajudam a expressar a lógica de forma clara e concisa.

### Conclusão

Funções de ordem superior são uma ferramenta poderosa para escrever código mais limpo, reutilizável e fácil de manter. Elas ajudam a abstrair lógica e promover uma abordagem mais funcional na programação, o que pode ser muito útil, especialmente ao manipular coleções de dados ou ao trabalhar com lógica comum aplicada a diferentes partes do código.