# Estruturas condicionais

## O que é um Loop?

> **Um loop é uma estrutura que executa um bloco de código repetidamente enquanto uma condição for satisfeita.**
> 

Existem duas perguntas importantes em qualquer laço:

1. Quando repetir?
2. Quando parar?

---

## O que é o `while`?

O `while` significa literalmente:

> **"Enquanto..."**
> 

Sua ideia é extremamente simples.

```
Enquanto condição for verdadeira

↓

Execute o bloco

↓

Volte e teste novamente
```

---

## Sintaxe

Segundo o *Think Python*:

```python
while condicao:instrucoes
```

Observe.

Assim como o `if`.

Temos:

- condição;
- dois pontos;
- bloco indentado.

---

## Primeiro Exemplo

```python
contador = 1
while contador <= 5:
	print(contador)
	contador+=1
```

Resultado.

```
1

2

3

4

5
```

---

## Fluxograma

```
          contador <= 5 ?

             │

      ┌──────┴───────┐

      │              │

    True          False

      │              │

      ▼              ▼

print(contador)     Fim

contador +=1

      │

      └──────────────┘
```

## Regra de Ouro

> **Toda variável utilizada na condição de um `while` deve evoluir em direção ao fim do laço.**
> 

Essa é uma das regras mais importantes da programação.

---

## Comparando `if` e `while`

| `if` | `while` |
| --- | --- |
| Executa no máximo uma vez | Pode executar inúmeras vezes |
| Apenas decide | Decide e repete |
| Não retorna ao início | Sempre volta para testar a condição novamente |

---
## Debugando um Loop

O material **Debugging** recomenda observar como as variáveis mudam ao longo da execução. Em laços de repetição, isso é especialmente importante para descobrir por que um loop não termina ou termina cedo demais.

Exemplo.

```python
contador=1
while contador <= 3 :
	print(contador)
	contador+=1
```

Durante o debug podemos inspecionar:

```
contador

1

↓

2

↓

3

↓

4
```

Assim verificamos que a condição de parada foi alcançada corretamente.

--- 

## Erros comuns

1. Esquecer de atualizar a variável
2. Atualizar a variável incorretamente
3. Condição impossível
4. Alterar a variável errada

--- 

## Boas Práticas

- Sempre identifique claramente a condição de parada.
- Atualize a variável responsável pela condição.
- Utilize nomes descritivos (`contador`, `tentativas`, `saldo`).
- Teste laços com poucos valores antes de ampliá-los.
- Utilize o depurador para acompanhar cada iteração.

--- 

## Resumo

| Conceito | Definição |
| --- | --- |
| Loop | Estrutura que repete um bloco de código |
| `while` | Executa um bloco enquanto uma condição for verdadeira |
| Iteração | Cada execução do corpo do laço |
| Condição de parada | Expressão que determina quando o laço termina |
| Loop infinito | Laço cuja condição nunca se torna falsa |

---

# O laço `for`- Iterando sobre sequências

## O que é o `for`?

> **O `for` executa um bloco de código para cada elemento de uma sequência.**
> 

Enquanto o `while` pergunta:

> "Ainda devo continuar?"
> 

O `for` pergunta:

> "Existe mais um elemento?"
> 

---

## Primeira Sintaxe

```
for item in sequencia:
	instrucoes
```

Observe.

Temos.

- variável da iteração;
- palavra `in`;
- sequência;
- bloco indentado.

---

## Primeiro Exemplo

```python
nomes= ["Ana","Lucas","Maria"
]
for nome in nomes:
	print(nome)
```

Resultado.

```
Ana

Lucas

Maria
```
---
Sempre se perguntar.

> **Estou repetindo uma ação sobre vários elementos?**
> 

Se sim.

Provavelmente o `for` é a melhor escolha.

Exemplos.

- percorrer nomes;
- percorrer produtos;
- percorrer linhas de um arquivo;
- percorrer caracteres de uma palavra.

---

## O `range()`

Muitas vezes queremos repetir uma ação um número específico de vezes.

Python fornece a função `range()`.

Exemplo.

```python
for numero in range(5):
	print(numero)

    # Resultado
    # 0
    # 1
    # 2
    # 3
    # 4
```

## Outro exemplo

```python
for numero in range(1,6):
	print(numero)

    # Resultado
    # 1
    # 2
    # 3
    # 4
    # 5
```

## Três parâmetros

```python
for numero in range(2,11,2):
	print(numero)

    # Resultado
    # 2
    # 4
    # 6
    # 8
    # 10
```
Também podemos contar de trás para frente.

```python
for numero in range(10,0,-1):
	print(numero)

    # Resultado
    # 10
    # 9
    # 8
    # 7
    # ...
    # 1
```
## Comparando `while` e `for`

| `while` | `for` |
| --- | --- |
| Controlado por condição | Controlado por sequência |
| Pode repetir indefinidamente | Termina quando a sequência acaba |
| Exige atualização manual | Atualização automática |
| Ideal para eventos desconhecidos | Ideal para coleções |

## Quando usar cada um?

Use **`while`** quando:

- não sabe quantas repetições existirão;
- espera uma condição;
- trabalha com menus;
- valida entradas do usuário.

---

Use **`for`** quando:

- percorre listas;
- percorre strings;
- percorre arquivos;
- conhece a quantidade de repetições.

---

## Debugando um `for`

O material **Debugging** recomenda inspecionar a variável da iteração para entender o comportamento do laço.

Exemplo.

```python
for nome in nomes:
	print(nome)
```
---
## Erros comuns

1. Alterar a coleção durante a iteração
2. Esperar que `range(5)`produza o número 5
3. Usar `while` quando um `for` seria o suficiente
4. Utilizar nomes pouco descritivos

---

## Boas Práticas

- Utilize `for` para percorrer sequências.
- Escolha nomes significativos para a variável da iteração.
- Prefira `range()` quando o objetivo for repetir um número conhecido de vezes.
- Não modifique a coleção que está sendo percorrida, salvo quando souber exatamente o impacto dessa alteração.

## Resumo

| Conceito | Definição |
| --- | --- |
| `for` | Percorre uma sequência de elementos |
| Iteração | Cada passagem pelo corpo do laço |
| `range()` | Gera uma sequência numérica |
| Sequência | Estrutura percorrível, como listas e strings |
| Variável da iteração | Recebe um elemento diferente a cada repetição |

---

# `break`, `continue`, `else` em Laços e Boas Práticas

## O que é o `break`?

> **O `break` interrompe imediatamente o laço.**
> 

Não importa quantas repetições ainda existiriam.
O laço termina naquele instante.

## Exemplo

```python
for numero in range(10):
	if numero == 5:
		break 
print(numero)

# 0
# 1
# 2
# 3
# 4
```

## O que é o `continue`?

> **O `continue` interrompe apenas a iteração atual.**
> 

O laço continua normalmente.

---

## Exemplo
```python
for numero in range(6):
	if numero ==3 :
		continue 
	print(numero)

# 0
# 1
# 2
# 4
# 5
# O três foi ignorado, mas o laço continuou
```

Pergunte.

> **Quero parar completamente ou apenas ignorar um caso?**
> 

Se deseja parar.

Use: `break

Se deseja apenas ignorar.

Use: `continue`

---
## O `else` nos Laços

Uma característica pouco conhecida do Python.

O `while` e o `for` podem possuir um bloco `else`. Esse bloco é executado **apenas quando o laço termina naturalmente**, isto é, sem que um `break` seja executado.

## Exemplo

```python
for numero in range(5):
	print(numero)
else:
	print("Fim")
	
# 0
# 1
# 2
# 4
# 5
# Fim
```

## Laços Aninhados

Assim como `if`.

Também podemos aninhar laços.

```python
for linha in range(3):
	for coluna in range(3):
		print(linha,coluna)
```

Fluxo.

```
Linha 0

↓

Coluna 0

↓

Coluna 1

↓

Coluna 2

↓

Linha 1

↓

...
```

## Comparação Geral

| Estrutura | Função |
| --- | --- |
| `while` | Repetir enquanto uma condição for verdadeira |
| `for` | Percorrer uma sequência |
| `break` | Encerrar imediatamente o laço |
| `continue` | Ignorar apenas a iteração atual |
| `else` | Executar quando o laço termina naturalmente |

---

## Erros comuns
1. Usar `break` quando queria `continue`
2. Criar vários níveis de repetição
3. Esquecer que `break` impede o else
4. Utilizar `While True` sem condição de saída

---
## Boas Práticas

- Utilize `break` apenas quando realmente precisar interromper o fluxo.
- Prefira `continue` para ignorar casos excepcionais.
- Evite laços excessivamente aninhados.
- Utilize nomes claros para variáveis de iteração.
- Depure acompanhando a evolução das variáveis.

---

## Resumo

| Conceito | Definição |
| --- | --- |
| `break` | Encerra imediatamente o laço |
| `continue` | Ignora a iteração atual |
| `else` em laços | Executa apenas quando o laço termina sem `break` |
| Laços aninhados | Um laço dentro de outro |
| Depuração | Acompanhamento da execução e do estado das variáveis |