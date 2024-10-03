A principal diferença entre **`sort()`** e **`sorted()`** em Python está na forma como elas manipulam a lista ou o iterável e no retorno de cada função:

### 1. **`sort()`**
- **Método de lista**: `sort()` é um método específico para listas e só pode ser chamado em objetos do tipo `list`.
- **Modifica a lista in-place**: Ela **altera a lista original**, ordenando seus elementos diretamente e **não retorna** um novo objeto. Em vez disso, retorna `None`, deixando claro que a operação foi feita in-place.
- **Exemplo**:
  ```python
  lista = [3, 1, 4, 1, 5]
  lista.sort()  # Ordena a lista in-place
  print(lista)  # Resultado: [1, 1, 3, 4, 5]
  ```

### 2. **`sorted()`**
- **Função embutida**: `sorted()` é uma função **global** que pode ser aplicada a qualquer iterável (como listas, tuplas, strings, dicionários, etc.), não se limitando apenas a listas.
- **Cria uma nova lista**: Ela **não altera o iterável original**. Em vez disso, retorna uma **nova lista** com os elementos ordenados.
- **Exemplo**:
  ```python
  tupla = (3, 1, 4, 1, 5)
  nova_lista = sorted(tupla)  # Cria uma nova lista ordenada
  print(nova_lista)  # Resultado: [1, 1, 3, 4, 5]
  print(tupla)  # A tupla original permanece inalterada
  ```

### Resumo das Diferenças:

| **Característica**      | **`sort()`**                   | **`sorted()`**                       |
|-------------------------|--------------------------------|--------------------------------------|
| **Tipo**                | Método de lista                | Função embutida                      |
| **Alteração do original** | Altera a lista in-place        | Não altera o original, cria nova lista |
| **Retorno**             | Retorna `None`                 | Retorna uma nova lista ordenada      |
| **Aplicável a**         | Apenas listas                  | Qualquer iterável                    |

### Quando usar:
- Use **`sort()`** quando você quiser **ordenar uma lista existente** e não se importar em modificar o objeto original.
- Use **`sorted()`** quando precisar **preservar o iterável original** ou quando estiver lidando com outros tipos de iteráveis, como tuplas ou strings, e precisar de uma **nova lista ordenada**.