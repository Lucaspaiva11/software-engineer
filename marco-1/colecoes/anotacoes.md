# Coleções

> **Uma coleção é uma estrutura que permite armazenar vários valores em uma única variável.**
>

## Lista
> **Uma lista é uma coleção ordenada de elementos: números,textos,booleanos,objetos e até outras listas**
```python
nomes = ["Ana", "Lucas", "Maria"]
```
**Pense numa estante: cada posição guarda um livro, e para encontrar um, basta informar sua posição.Uma lista funciona exatamente assim.**

Cada elemento tem uma posição chamada `Índice`, começando em 0.
*Listas são mutáveis* - Seus elementos podem ser mudados depois de criados
Uma lista com três elementos tem *índices*: `0`,`1`,`2`-> não existe índice `3`.

---

## Operações com listas
## Adicionando elementos

```python
nomes = ["Ana", "Lucas"]
nomes.append("Maria")     # adiciona no final
# ['Ana', 'Lucas', 'Maria']

nomes2 = ["Ana", "Maria"]
nomes2.insert(1, "Lucas")  # insere numa posição específica
# ['Ana', 'Lucas', 'Maria']
```

## Removendo elementos

```python
nomes.remove("Lucas")   # remove pelo VALOR (primeira ocorrência)
nomes.pop(1)              # remove pelo ÍNDICE
nomes.clear()              # remove todos os elementos → []
```

| `remove()` | `pop()` |
| --- | --- |
| Remove pelo **valor** | Remove pelo **índice** (e retorna o elemento removido) |

## Concatenando e repetindo

```python
lista1 = [1, 2]
lista2 = [3, 4]
resultado = lista1 + lista2   # [1, 2, 3, 4]

numeros = [1, 2]
print(numeros * 3)              # [1, 2, 1, 2, 1, 2]
```

## Operador `in`

```python
print("Lucas" in nomes)   # True — "Lucas está nesta lista?"
print("Pedro" in nomes)   # False
```

## Fatiamento (*slicing*)

```python
nomes = ["Ana", "Lucas", "Maria", "Pedro"]
print(nomes[1:3])   # ['Lucas', 'Maria'] — o índice final NÃO é incluído

copia = nomes[:]     # cria uma cópia (nova lista com os mesmos elementos)
```

## Percorrendo uma lista

```python
for nome in nomes:
    print(nome)          # forma preferida — mais simples e legível

for i in range(len(nomes)):
    print(nomes[i])       # use apenas quando realmente precisar da posição
```
---

## Mutabilidade, referências, aliasing e cópias
```python
lista1 = [1, 2, 3]
lista2 = lista1   # lista2 NÃO é uma cópia — é outra referência para o MESMO objeto
```

```
lista1 ───┐
          ▼
      [1, 2, 3]
          ▲
lista2 ───┘
```

## Aliasing

```python
lista2.append(4)
print(lista1)   # [1, 2, 3, 4] — lista1 também mudou!
```

Isso acontece porque `lista1` e `lista2` apontam para o **mesmo** objeto — esse compartilhamento acidental é chamado de ***aliasing*** e é uma das maiores fontes de bugs envolvendo listas.

>  Pergunta-guia: *criei uma nova lista, ou apenas outra variável apontando para a mesma lista?*
> 

## Igualdade × identidade

```python
lista1 = [1, 2]
lista2 = lista1
lista3 = [1, 2]

lista1 is lista2   # True  — mesmo objeto
lista1 is lista3   # False — objetos diferentes, mesmo com conteúdo igual
lista1 == lista3   # True  — compara CONTEÚDO, não identidade
```

| `==` | `is` |
| --- | --- |
| Compara **conteúdo** | Compara **identidade** (é o mesmo objeto?) |

## Criando uma cópia de verdade

```python
copia = lista.copy()   # ou lista[:]
copia.append(4)
print(lista)   # permanece inalterada — copia é um objeto independente
```

## Listas aninhadas (matrizes)

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz[0]      # [1, 2, 3]
matriz[0][0]   # 1
matriz[2][1]   # 8
```

Para percorrer, aninhamos dois `for`:

```python
for linha in matriz:
    for numero in linha:
        print(numero)
```
---
## Tuplas, conjuntos(set) e dicionários
## Tuplas — coleção ordenada e imutável

```python
coordenada = (10, 20)
cores = ("Azul", "Verde", "Vermelho")

coordenada[0] = 50
# TypeError — a tupla é imutável, não pode ser alterada
```

>  Como uma coordenada GPS: latitude e longitude representam uma única informação — não faz sentido alterar apenas uma parte aleatoriamente. A tupla protege os dados contra modificações acidentais.
> 

**Use tuplas para:** coordenadas, datas, horários, valores constantes — informações que não devem mudar.

## Conjuntos (`set`) — sem ordem, sem duplicados

```python
frutas = {"Maçã", "Banana", "Laranja"}

numeros = {1, 2, 2, 3, 3, 3}
print(numeros)   # {1, 2, 3} — duplicados desaparecem automaticamente

frutas.add("Uva")
frutas.remove("Banana")
print("Maçã" in frutas)   # True
```

>  Como um álbum de figurinhas: você pode ter três figurinhas repetidas, mas no álbum ela aparece só uma vez.
> 

**Use `set` para:** remover duplicados, verificar existência rapidamente, representar elementos únicos.

## Dicionários (`dict`) — pares chave → valor

```python
usuario = {"nome": "Lucas", "idade": 21, "cidade": "São Paulo"}

print(usuario["nome"])    # Lucas
usuario["idade"] = 22       # altera um valor
usuario["profissao"] = "Desenvolvedor"   # adiciona um novo campo

for chave, valor in usuario.items():
    print(chave, valor)
```

>  Como uma ficha de cadastro: cada informação tem um nome (`Nome → Lucas`, `Idade → 21`).
> 

>  Objetos JSON de APIs (`{"id": 10, "nome": "Lucas"}`) têm comportamento muito parecido com dicionários Python.
> 

Acessar uma chave que não existe (`usuario["telefone"]`) gera **`KeyError`**.

**Use `dict` para:** representar entidades com atributos nomeados, dados de APIs, configurações.

##  Comparação geral

| Estrutura | Ordenada | Mutável | Duplicados | Acesso principal |
| --- | --- | --- | --- | --- |
| Lista | ✅ | ✅ | ✅ | Índice |
| Tupla | ✅ | ❌ | ✅ | Índice |
| Set | ❌ | ✅ | ❌ | Valor |
| Dict | Preserva ordem de inserção | ✅ | Chaves únicas | Chave |

##  Fluxograma de escolha

```
Tenho vários dados?
        │
       Sim
        │
Preciso de nomes para cada dado? ──Sim──► Dict
        │
       Não
        │
Preciso de elementos únicos? ──Sim──► Set
        │
       Não
        │
Os dados podem mudar? ──Sim──► Lista
        │
       Não
        │
       Tupla
```
---
## Depuração de coleções

Ao investigar comportamento inesperado numa lista, inspecione o **conteúdo antes e depois** de cada operação (inserção, remoção) e o valor do índice usado. Muitos bugs "misteriosos" com listas não estão na lógica da função, mas no compartilhamento acidental da mesma lista entre variáveis (*aliasing*) — sempre que uma alteração aparece "sozinha" em outra variável, verifique se as duas não apontam para o mesmo objeto.

---

## Boas práticas

- Escolha nomes que representem o conjunto (`alunos`, `produtos`, `notas`)
- Prefira `for elemento in lista` a usar índices, salvo quando a posição for realmente necessária
- Use `in` para verificar pertencimento em vez de percorrer manualmente
- Use `copy()` (ou `lista[:]`) sempre que precisar de uma lista **independente**
- Prefira `==` para comparar valores; use `is` só para verificar identidade de objeto
- Escolha a coleção pela **natureza do problema**, não por familiaridade — listas para sequências mutáveis, tuplas para dados fixos, sets para unicidade, dicts para dados nomeados

---

## Resumo geral

| Conceito | Definição |
| --- | --- |
| Coleção | Estrutura que armazena vários valores |
| Lista | Coleção ordenada e **mutável** |
| Índice | Posição de um elemento (começa em 0) |
| `len()` | Quantidade de elementos |
| `append()` / `insert()` | Adiciona ao final / numa posição específica |
| `remove()` / `pop()` | Remove pelo valor / pelo índice |
| `in` | Verifica pertencimento |
| *Slicing* | Obtém uma parte da lista (limite final exclusivo) |
| Mutabilidade | Objeto pode ser alterado após sua criação |
| Referência / *Aliasing* | Ligação variável↔objeto / múltiplas variáveis apontando para o mesmo objeto |
| `copy()` | Cria uma cópia independente (rasa) |
| `==` / `is` | Compara conteúdo / compara identidade |
| Tupla | Coleção ordenada e **imutável** |
| Set | Coleção sem ordem e **sem duplicados** |
| Dict | Coleção de pares **chave → valor** |
| `IndexError` / `ValueError` / `KeyError` | Índice inexistente / valor inválido / chave inexistente |