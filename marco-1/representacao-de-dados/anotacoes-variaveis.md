# Variáveis: como o programa se lembra das informações

## Variável
> **Uma variável é um nome utilizado para referenciar um valor durante a execução de um programa. (Espaço alocado na memória para armazenar valores, e as variáveis tem nome para podermos acessa esses valores posteriormente)**
>

Exemplo:
```
┌──────────────┐
│    Nome      │
├──────────────┤
│ Lucas        │
└──────────────┘

┌──────────────┐
│    Idade     │
├──────────────┤
│ 20           │
└──────────────┘

┌──────────────┐
│    Saldo     │
├──────────────┤
│ 1500.50      │
└──────────────┘
```
---
# Atribuição
- Associação entre um nome e um valor
> **O "=" não representa igualdade e sim associa/atribui o valor aquela variável**
>

```
nome = valor

Exemplo -> idade = 20
```

# Estado do Programa
Durante a execução, os valores associados ás variáveis podem mudar. O conjunto desses valores em um determinado instante representa o **estado do programa**

## Exemplo

```
saldo = 100
```

Estado.

```
saldo

↓

100
```

---

Depois.

```
saldo = saldo + 50
```

Novo estado.

```
saldo

↓

150
```
> **Variável permaneceu, já o valor mudou**
>

---

# Nomes de variáveis
Importante dar bons nomes pois o código é lido mais vezes do que é escrito

**Bons exemplos** -> `idade`, `salario`, `total_pedido`
**Maus exemplos** -> a`, `x1`, `teste2`

# Convenções em python
Em Python nomes utilizam snake_case

**Exemplos** 
Deve ser feito -> `nome_cliente`, `valor_total`
Evite-> nomeCLiente`, `valorTotal`

## Constantes
Em python não possui tipagem de constante
Por convenção eles são escritos em maiusculas

**Exemplos** -> `PI = 3.14159`, `IDADE_MINIMA = 18`

# Boas práticas

- Escolher nomes claros e específicos.
- Uma variável deve representar apenas uma informação.
- Prefira nomes completos a abreviações obscuras.
- Utilize constantes (em maiúsculas) para valores fixos.
- Acompanhe mentalmente o estado do programa enquanto desenvolve.

# 📖 Resumo

| Conceito | Definição |
| --- | --- |
| Variável | Nome que referencia um valor |
| Valor | Informação armazenada pelo programa |
| Atribuição | Associação entre um nome e um valor |
| Estado do programa | Conjunto de valores das variáveis em um instante da execução |
| Identificador | Nome dado a uma variável |
| Constante (convenção) | Variável cujo nome é escrito em maiúsculas para indicar que seu valor não deve ser alterado |