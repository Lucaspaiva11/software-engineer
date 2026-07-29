# Como tomar decisões?

## O que é o IF?
> **O `if` permite executar um bloco de código apenas quando uma condição é verdadeira.**
> 

Essa é uma das estruturas mais importantes de toda a programação.
Sem ela.
Programas não tomam decisões.

### Exemplo:
```python
idade = 20
if idade >= 18:
    print('Maior de idade')
```

    Sempre pergunte.

> **Existe alguma situação em que uma parte do programa deve executar apenas às vezes?**
> 

Se a resposta for sim.

Provavelmente você precisa de um `if`.

Por exemplo.

- liberar acesso;
- aplicar desconto;
- validar senha;
- verificar estoque;
- aprovar pagamento.

---

## Boas Práticas

- Escreva condições simples e fáceis de entender.
- Utilize nomes descritivos para variáveis booleanas (`esta_logado`, `pagamento_aprovado`).
- Evite blocos muito grandes dentro de um único `if`.
- Indente sempre com quatro espaços, conforme a convenção da comunidade Python (PEP 8).

## Resumo

| Conceito | Definição |
| --- | --- |
| `if` | Executa um bloco de código apenas quando uma condição é verdadeira |
| Condição | Expressão que produz `True` ou `False` |
| Bloco | Conjunto de instruções pertencentes ao `if` |
| Indentação | Define os blocos de código em Python |
| Fluxo de execução | Caminho percorrido pelo programa durante sua execução |

---

## ELSE
> **O `else` define o bloco que será executado quando a condição do `if` for falsa.**
> 

Assim, sempre um dos caminhos será executado.

## ELIF
> **O `elif` adiciona novas condições entre o `if` e o `else`.**
> 

Ele significa literalmente:

> **"Else If"**
> 

ou

> "Senão, se..."
>

---

# Boas Práticas

- Ordene as condições da mais específica para a mais geral.
- Utilize `elif` quando apenas uma alternativa deve ser escolhida.
- Utilize `else` para tratar casos não previstos explicitamente.
- Escreva condições mutuamente exclusivas sempre que possível.

---
# Resumo

| Conceito | Definição |
| --- | --- |
| `else` | Executa quando o `if` é falso |
| `elif` | Adiciona novas condições à mesma decisão |
| Fluxo exclusivo | Apenas um bloco é executado |
| Ordem das condições | O Python avalia de cima para baixo |

---

# Condições aninhadas
> **Uma condicional aninhada é um `if` dentro de outro `if`.**
> 

Exemplo.

```python
idade=20
possui_carteira=True
if idade >= 18:
	if possui_carteira:
		print("Pode dirigir")
```

## Como evitar condições aninhadas
Muitas vezes podemos combinar condições.

Em vez de:

```python
if usuario:
	if ativo:
		print("Acesso")
```

Podemos escrever.

```python
if usuario and ativo:
	print("Acesso")
```

Mais simples.

Mais legível.

---

# Operador Ternário

Python permite escrever um `if` simples em apenas uma linha.

Sintaxe.

```
valor_se_verdadeiro if condicao else valor_se_falso
```

Exemplo.

```python
idade=20
resultado="Adulto"
if idade >= 18 else"Menor"
```

Resultado.

```
Adulto
```

---

## Comparação

Forma tradicional.

```python
if idade >= 18:
	categoria = "Adulto"
else:
	categoria="Menor"
```

Forma reduzida.

```python
categoria = "Adulto"
if idade >= 18 else"Menor"
```

---

# Quando utilizar?

Use apenas quando a expressão for pequena.

Boa utilização.

```python
status="Online"
if conectado else "Offline"
```

Má utilização.

```
resultado= ...if ...else ...if ...else ...
```

Expressões grandes prejudicam a leitura.

--- 
# Match

```
match comando:
	case"iniciar":
		print("Sistema iniciado")
	case"parar":
		print("Sistema encerrado")
	case_:
		print("Comando inválido")
```
Ele é especialmente útil quando queremos comparar um mesmo valor contra várias possibilidades.

## Quando usar `if` e quando usar `match`?

| Situação | Melhor escolha |
| --- | --- |
| Comparações simples | `if` |
| Expressões booleanas | `if` |
| Intervalos (`idade >= 18`) | `if` |
| Muitos valores fixos | `match` |

---

# Debugando condicionais

```python
idade=17
if idade >= 18:
    # print(idade)
    # Use antes de alterar o código para entender o porque a condição não foi satisfeita
	print("Adulto")

```
Internamente.

```
Avalia condição

↓

Resultado booleano

↓

Escolhe apenas um caminho

↓

Executa o bloco escolhido

↓

Ignora completamente o outro bloco

↓

Continua programa
```
---

## Lendo a condição

Separar a condição.

```python
condicao = idade >=18
print(condicao)

# Resultado -> False
# Isso facilita a investigação
```
> Primeiro reproduzir e compreender o problema antes de tentar corrigi-lo(debugar)

---
## Boas Práticas

- Prefira condições simples.
- Evite muitos níveis de aninhamento.
- Utilize `elif` quando apenas um caminho deve ser executado.
- Utilize `match` quando comparar muitos valores fixos.
- Depure observando o estado das variáveis antes de modificar o código.
- Escreva código pensando em quem irá lê-lo no futuro.