# Modelo de dados 

## Objetos em python
## O que é um objeto?

Um **objeto**, em Python, é uma região de memória que guarda um valor, um tipo, e (dependendo do tipo) atributos e métodos associados a ele. Cada objeto tem um identificador único de memória, acessível através da função `id()`.

```python
numero = 42
print(type(numero))  # <class 'int'>
print(id(numero))    # algum endereço de memória, ex: 4302021840
```

## Variáveis não são caixas — são etiquetas

Diferente da metáfora usada na Parte 2 (Capítulo 1), agora é hora de refinar essa imagem: uma variável em Python **não é** a caixa que guarda o valor — ela é apenas uma **etiqueta (nome)** apontando para um objeto que existe independentemente dela na memória.

```
numero  ────aponta para────▶  [ objeto int, valor 42, id 4302021840 ]
```
---

## Referências

Se uma variável é apenas uma etiqueta apontando para um objeto (Capítulo 1), o que acontece quando você atribui uma variável a outra?

```python
lista_a = [1, 2, 3]
lista_b = lista_a
```

> Isso não cria uma segunda lista, cria uma **segunda etiqueta** apontando para exatamente o mesmo objeto na memória. É como colar um segundo apelido na mesma caixa, em vez de criar uma caixa nova.
> 

## Referência em ação

```
lista_a ──┐
          ├──▶ [ 1, 2, 3 ]   (um único objeto na memória)
lista_b ──┘
```

```python
lista_a = [1, 2, 3]
lista_b = lista_a
lista_b.append(4)

print(lista_a)  # [1, 2, 3, 4]  lista_a também mudou!
print(lista_b)  # [1, 2, 3, 4]
print(lista_a is lista_b)  # True — são o mesmo objeto
```

---

## Mutabilidade

## O que significa ser mutável?

Um tipo é **mutável** quando seu conteúdo pode ser alterado depois de criado, mantendo o mesmo identificador de memória (`id()`).

```python
lista = [1, 2, 3]
print(id(lista))     # ex: 140234
lista.append(4)
print(id(lista))     # o mesmo id — o objeto original foi modificado, não substituído
```

## Tipos mutáveis mais comuns

| Python | TypeScript / JavaScript |
| --- | --- |
| `list` | `Array` |
| `dict` | `Object` |
| `set` | `Set` |

---

## Imutabilidade

## O que significa ser imutável?

Um tipo é **imutável** quando, uma vez criado, seu valor nunca pode ser alterado — qualquer operação que "parece" modificá-lo, na verdade, cria um **novo objeto** e reatribui a variável a esse novo objeto.

```python
x = 10
print(id(x))     # ex: 4297936592 (o objeto "10" na memória)
x = x + 1
print(id(x))     # um id DIFERENTE — x agora aponta para um novo objeto "11"
```

```
Antes:  x ──▶ [ objeto int 10 ]
Depois: x ──▶ [ objeto int 11 ]     (o objeto "10" continua existindo até ser descartado)
```

## Tipos imutáveis mais comuns

| Python | TypeScript / JavaScript |
| --- | --- |
| `int`, `float`, `bool` | `number`, `boolean` |
| `str` (já visto na Parte 2) | `string` |
| `tuple` | — (não há equivalente direto nativo) |

## Mutável × Imutável

| Característica | Mutável | Imutável |
| --- | --- | --- |
| Alteração "no lugar"? | Sim | Não — sempre cria um novo objeto |
| Duas variáveis podem "vazar" alterações entre si? | Sim, se apontarem pro mesmo objeto | Não, nunca |
| Exemplos | `list`, `dict`, `set` | `int`, `str`, `tuple`, `bool` |

---

## Identidade X igualdade

## `==` (igualdade de valor) × `is` (identidade)

```python
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]      # uma lista DIFERENTE, com o mesmo conteúdo
lista_c = lista_a         # a MESMA lista que lista_a

print(lista_a == lista_b)  # True  — mesmo conteúdo (igualdade)
print(lista_a is lista_b)  # False — objetos diferentes na memória (identidade)
print(lista_a is lista_c)  # True  — o mesmo objeto (identidade)
```

```
lista_a ──┐
          ├──▶ [ 1, 2, 3 ]   objeto #1
lista_c ──┘

lista_b ──▶ [ 1, 2, 3 ]      objeto #2 (conteúdo igual, objeto diferente)
```
### Comparação especial de `None`/`null`

Por convenção, compara-se ausência de valor com `is`/identidade, não com `==`, tanto porque só existe uma única instância de `None` na memória de um programa Python:

```python
valor = None
if valor is None:   # convenção recomendada em Python
    print("sem valor")
```

---

## Cópia Rasa

Uma **cópia rasa** cria um novo objeto "de primeiro nível", mas os elementos **dentro** dele (se forem, por sua vez, objetos mutáveis) continuam sendo as mesmas referências do objeto original.

```python
import copy

original = [[1, 2], [3, 4]]
copia = copy.copy(original)  # ou original[:] ou list(original)

copia.append([5, 6])      # afeta só a cópia — o nível externo é realmente novo
print(original)           # [[1, 2], [3, 4]]

copia[0].append(99)       # ⚠️ modifica o objeto interno, que é COMPARTILHADO
print(original)           # [[1, 2, 99], [3, 4]]  ← o original também mudou!
```

```
original ──▶ [ ref1, ref2 ]        cópia ──▶ [ ref1, ref2 ]    (nível externo: objetos diferentes)
                │      │                          │      │
                ▼      ▼                          ▼      ▼
             [1,2]   [3,4]  ◀── mesmos objetos internos, compartilhados ──▶
```

---
## Cópia Profunda

## O que é uma cópia profunda?

Uma **cópia profunda** cria um novo objeto em **todos os níveis**, recursivamente — nenhum objeto interno é compartilhado com o original, não importa o quão aninhado ele esteja.

```python
import copy

original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(original)

copia_profunda[0].append(99)
print(original)         # [[1, 2], [3, 4]]  — o original NÃO mudou
print(copia_profunda)   # [[1, 2, 99], [3, 4]]
```

## Cópia Rasa × Cópia Profunda

| Característica | Cópia Rasa | Cópia Profunda |
| --- | --- | --- |
| Nível externo | Objeto novo | Objeto novo |
| Objetos internos (aninhados) | Compartilhados com o original | Também copiados, recursivamente |
| Custo de processamento | Menor | Maior (percorre toda a estrutura) |
| Quando usar | Estrutura "rasa", sem aninhamento mutável | Estruturas aninhadas que precisam de independência total |

---
## Garbage Collector (Visão Geral)

## Contagem de referências

O mecanismo principal do CPython (a implementação padrão de Python) é a **contagem de referências**: cada objeto guarda um contador de quantas variáveis (ou outros objetos) apontam para ele. Quando esse contador chega a zero, o objeto é liberado imediatamente.

```python
import sys

x = []
print(sys.getrefcount(x))  # 2 (x, mais a referência temporária do próprio getrefcount)

y = x
print(sys.getrefcount(x))  # 3 — agora y também referencia o mesmo objeto

del y
print(sys.getrefcount(x))  # 2 novamente
```

```
Criação:  x ──▶ [ objeto ]  (contagem = 1)
y = x:    x ──┐
              ├──▶ [ objeto ]  (contagem = 2)
          y ──┘
del y:    x ──▶ [ objeto ]  (contagem = 1)
del x:              [ objeto ]  (contagem = 0 → liberado da memória)
```

## O problema das referências cíclicas

A contagem de referências tem uma limitação conhecida: se dois objetos referenciam um ao outro (uma referência cíclica), o contador de ambos nunca chega a zero — mesmo que nada de fora aponte mais para eles.

```python
a = {}
b = {}
a["ref"] = b  # a referencia b
b["ref"] = a  # b referencia a — um ciclo

del a, b  # as referências externas somem, mas a e b ainda se referenciam mutuamente
```

Para esse caso, Python usa um segundo mecanismo, complementar: o **coletor cíclico geracional**, que roda periodicamente (não instantaneamente), procurando grupos de objetos que só se referenciam entre si e nada mais de fora aponta para eles, liberando-os.

## Os dois mecanismos, lado a lado

| Mecanismo | Quando age | O que resolve |
| --- | --- | --- |
| Contagem de referências | Imediatamente, assim que o contador chega a zero | A grande maioria dos casos |
| Coletor cíclico geracional | Periodicamente, em ciclos | Referências cíclicas, que a contagem sozinha não resolve |

---

## Resumo geral

| Conceito | Ideia principal |
| --- | --- |
| Objeto | Região de memória com valor, tipo e identificador único (`id()`) |
| Referência | Uma variável aponta para um objeto, em vez de "conter" o valor diretamente |
| Mutabilidade | O objeto pode ser alterado no lugar, mantendo o mesmo id |
| Imutabilidade | Qualquer "alteração" cria um novo objeto |
| Identidade × Igualdade | `is`/`===` compara referência; `==` compara valor |
| Cópia rasa | Novo objeto externo, objetos internos ainda compartilhados |
| Cópia profunda | Novo objeto em todos os níveis, recursivamente |
| Garbage Collector | Libera memória via contagem de referências, com um coletor cíclico complementar para referências circulares |