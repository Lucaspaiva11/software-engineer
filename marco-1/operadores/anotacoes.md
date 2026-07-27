# OPERADORES - Como um computador toma decisões e realiza cálculos

## Operadores
> **Um operador é um símbolo que indica ao intepretador qual será a operação realizada entre um ou mais valores**
>

Os operadores são responsáveis por transformar os dados em novos dados.

## Operando × Operador

Esses conceitos costumam ser confundidos.

Na expressão:

```
10+5
```

Temos:

```
10        +

5
│         │
│         └── Operador
│
└──────────── Operandos
```

Os **operandos** são os valores.

O **operador** determina o que fazer com eles.
---

## Os Operadores Aritméticos

Python

| Operador | Nome | Exemplo |
| --- | --- | --- |
| `+` | Soma | `10 + 5` |
| `-` | Subtração | `10 - 5` |
| `*` | Multiplicação | `10 * 5` |
| `/` | Divisão | `10 / 5` |
| `//` | Divisão inteira | `10 // 3` |
| `%` | Módulo (resto) | `10 % 3` |
| `**` | Potência | `2 ** 5` |

---
## Boas práticas

- Utilize parênteses para deixar a intenção clara.
- Evite expressões excessivamente longas.
- Armazene cálculos intermediários em variáveis quando isso melhorar a legibilidade.
- Antes de executar uma expressão, tente prever mentalmente o resultado.

---
## Resumo

| Conceito | Definição |
| --- | --- |
| Operador | Símbolo que realiza uma operação sobre operandos |
| Operando | Valor ou variável utilizada em uma operação |
| Expressão | Combinação de operandos e operadores que produz um valor |
| Precedência | Regras que determinam a ordem de avaliação das operações |
| `%` | Retorna o resto da divisão |
| `//` | Realiza divisão inteira |
| `**` | Calcula potências |

---

# Operadores de comparação e lógicos

## Operadores de Comparação

São operadores que comparam dois valores.

| Operador | Significado |
| --- | --- |
| `==` | Igual |
| `!=` | Diferente |
| `>` | Maior |
| `<` | Menor |
| `>=` | Maior ou igual |
| `<=` | Menor ou igual |

# Operadores Lógicos

## Operador AND

Significa.

> As duas condições precisam ser verdadeiras.
> 

---

Exemplo.

```python
idade>=18 and possui_ingresso
```

Só será verdadeiro se ambas forem verdadeiras.

---

## Tabela Verdade

| A | B | A and B |
| --- | --- | --- |
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## Operador OR
Significa.

> Basta uma condição ser verdadeira.
> 

---

Exemplo.

```python
possui_convite or nome_na_lista
```

---

## Tabela Verdade

| A | B | A or B |
| --- | --- | --- |
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## Operador NOT
Ele inverte o valor.

```python
not True
```

Resultado.

```
False
```

---

```python
not False
```

Resultado.

```
True
```

---

## Tabela

| Valor | not |
| --- | --- |
| True | False |
| False | True |

---

## Boas práticas

- Escreva condições que pareçam frases.
- Dê nomes significativos para variáveis booleanas (`possui_ingresso`, `esta_logado`, `pagamento_confirmado`).
- Utilize parênteses para melhorar a legibilidade de expressões complexas.
- Evite negar condições desnecessariamente (`not not valor`).
- Não comparar tipos diferentes.

---

## Resumo

| Conceito | Definição |
| --- | --- |
| Booleano | Tipo de dado com apenas dois valores: `True` e `False` |
| Operadores de comparação | Comparam valores e produzem um booleano |
| `and` | Verdadeiro apenas quando todas as condições são verdadeiras |
| `or` | Verdadeiro quando pelo menos uma condição é verdadeira |
| `not` | Inverte um valor booleano |
| Curto-circuito | Interrupção da avaliação quando o resultado já é conhecido |

---

# Operadores de Atribuição, precedência e Escrita de expressões

## Operadores de atribuição composta
## Resumo dos Operadores de Atribuição

Em Python:

| Operador | Equivale a |
| --- | --- |
| `+=` | `x = x + y` |
| `-=` | `x = x - y` |
| `*=` | `x = x * y` |
| `/=` | `x = x / y` |
| `//=` | `x = x // y` |
| `%=` | `x = x % y` |
| `**=` | `x = x ** y` |

---

# Ordem Geral

```
Parênteses

↓

Potência

↓

Multiplicação / Divisão / Módulo

↓

Soma / Subtração

↓

Comparações

↓

NOT

↓

AND

↓

OR
```

Essa é a ordem utilizada pelo interpretador para os operadores estudados até aqui.

---
## Legibilidade

Existe uma diferença enorme entre código que funciona e código que pode ser entendido.

Compare.

```python
if idade>=18 and saldo>1000 and ativo==True:
```

Agora.

```python
if (idade>=18 and saldo>1000 and ativo
):
```

Os dois fazem exatamente a mesma coisa.
Mas o segundo é muito mais fácil de ler.
---
## Expressões Pequenas

Evite.

```python
resultado=a+b*c-d/e+f*g-h+i-j*k+l/m
```

Prefira.

```python
subtotal=b*c
desconto=d/e
resultado=a+subtotal-desconto
```

Programas são escritos para pessoas lerem.
---

## Comparação com True

Evite.

```python
if ativo==True:
```

Prefira.

```python
if ativo:
```

Da mesma forma.

Evite.

```python
if ativo==False:
```

Prefira.

```python
if not ativo:
```

Essa é a convenção utilizada pela comunidade Python.