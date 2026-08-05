# Variáveis
## O que é uma variável?

Uma **variável** é um espaço nomeado na memória do computador que guarda um valor, permitindo que esse valor seja lido e (na maioria dos casos) alterado ao longo da execução do programa.

```
Nome da variável  →  aponta para  →  Endereço de memória  →  contém  →  Valor
      idade                              0x7ffee...                  25
```

Quando você escreve `idade = 25`, o computador reserva um espaço na memória, grava o valor `25` nele, e associa o nome `idade` a esse espaço — daí em diante, escrever `idade` no código é o mesmo que dizer "o valor guardado naquele espaço".

---
# Tipos primitivos

| Tipo | TypeScript | Python | Exemplo |
| --- | --- | --- | --- |
| Número inteiro | `number` | `int` | `42` |
| Número decimal | `number` | `float` | `3.14` |
| Texto | `string` | `str` | `"olá"` |
| Verdadeiro/falso | `boolean` | `bool` | `true` / `True` |
| Ausência de valor | `null` / `undefined` | `None` | — |

## Tipagem estática X Tipagem dinâmica

- **Tipagem estática** (TypeScript): o tipo de cada variável é verificado antes mesmo do programa rodar (em tempo de compilação).

- **Tipagem dinâmica** (Python): o tipo é verificado apenas durante a execução (em tempo de execução). 

| Característica | Tipagem estática | Tipagem dinâmica |
| --- | --- | --- |
| Erros de tipo | Detectados antes de rodar | Detectados só durante a execução |
| Velocidade de escrita | Mais verbosa | Mais rápida de escrever |
| Segurança em projetos grandes | Maior | Menor (sem ferramentas extras) |
| Flexibilidade | Menor | Maior |

--- 
# Operadores

Guardar valores em variáveis só é útil se pudermos combiná-los, compará-los e tomar decisões com base neles. É isso que os operadores fazem.

## Operadores aritméticos

| Operador | Significado | Exemplo |
| --- | --- | --- |
| `+` | Soma | `2 + 3 → 5` |
| `-` | Subtração | `5 - 2 → 3` |
| `*` | Multiplicação | `4 * 2 → 8` |
| `/` | Divisão | `7 / 2 → 3.5` |
| `%` | Resto da divisão (módulo) | `7 % 2 → 1` |
| `**` (Python) / `**` (TS) | Potência | `2 ** 3 → 8` |

## Operadores relacionais

Comparam dois valores e sempre produzem um booleano (`true`/`false`): `==` (igual), `!=` (diferente), `>`, `<`, `>=`, `<=`.

> ⚠️ Em TypeScript, prefira sempre `===` (igualdade estrita, compara valor **e** tipo) em vez de `==` (igualdade solta, converte tipos antes de comparar) — `"5" == 5` é `true`, mas `"5" === 5` é `false`. Essa armadilha é uma das mais citadas em entrevistas de JavaScript/TypeScript.
> 

## Operadores lógicos

| Operador | Significado |
| --- | --- |
| `&&` (TS) / `and` (Python) | Verdadeiro só se ambos forem verdadeiros |
| `||` (TS) / `or` (Python) | Verdadeiro se pelo menos um for verdadeiro |
| `!` (TS) / `not` (Python) | Inverte o valor lógico |

## Ordem de precedência (introdução)

| Prioridade | Operadores |
| --- | --- |
| 1 | `( )` |
| 2 | `**` |
| 3 | `* / // %` |
| 4 | `+ -` |

---
# Entrada e Saída
Um programa que não recebe nenhuma entrada e não produz nenhuma saída visível não tem utilidade prática nenhuma para quem o usa

## Saída (output)

```tsx
console.log("Olá, mundo!");
```
```python
print("Olá, mundo!")
```

## Entrada (input)
```python
nome = input("Qual o seu nome? ")
print(f"Olá, {nome}!")
```
---

# Conversão de Tipos
## Conversão explícita (casting)

```tsx
const texto: string = "25";
const numero: number = Number(texto);      // 25
const comoTexto: string = String(numero);  // "25"
```

```python
texto = "25"
numero = int(texto)      # 25
como_texto = str(numero) # "25"
```

## Conversão implícita (coerção)

Algumas linguagens convertem tipos automaticamente, sem o programador pedir — isso é chamado de **coerção implícita**, e é uma fonte comum de bugs sutis.

```tsx
console.log("5" + 3);   // "53"  → o número foi convertido para texto e concatenado
console.log("5" - 3);   // 2     → aqui o texto foi convertido para número
```

```python
# Python é mais restritivo: não faz coerção implícita entre str e int
"5" + 3   # TypeError: can only concatenate str (not "int") to str
```

>  Essa diferença de comportamento entre `+` (que em TypeScript prioriza concatenar texto) e `-`/`*`/`/` (que forçam conversão para número) é uma armadilha clássica de entrevista técnica em JavaScript/TypeScript.
>

---

# Expressões
Até aqui vimos variáveis, operadores e conversões isoladamente. Uma **expressão** é a combinação de tudo isso numa única unidade que, quando avaliada, produz um valor.

## Expressão × Comando (statement)

- **Expressão**: produz um valor. Ex.: `2 + 3`, `idade >= 18`, `nome.toUpperCase()`.
- **Comando (statement)**: executa uma ação, mas não necessariamente produz um valor a ser usado. Ex.: `let x = 10;`, um laço `for` inteiro, uma declaração de função.

```
idade >= 18           ← expressão (produz true ou false)
if (idade >= 18) { }  ← comando (usa o resultado da expressão para decidir algo)
```
---

# Strings

## Declarando e concatenando strings

```tsx
const primeiroNome: string = "Ana";
const sobrenome: string = "Silva";
const nomeCompleto: string = primeiroNome + " " + sobrenome; // "Ana Silva"
```

```python
primeiro_nome = "Ana"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome  # "Ana Silva"
```

## Indexação e fatiamento (slicing)

Uma string é, por baixo dos panos, uma sequência ordenada de caracteres — cada caractere tem uma posição (índice), começando em `0`.

```
Índice:    0   1   2   3   4
String:    P   y   t   h   o   n
```

```tsx
const linguagem = "Python";
console.log(linguagem[0]);        // "P"
console.log(linguagem.slice(0, 3)); // "Pyt"
```

```python
linguagem = "Python"
print(linguagem[0])      # "P"
print(linguagem[0:3])    # "Pyt"
```

## Strings são imutáveis

Em ambas as linguagens, uma string **não pode ser alterada no lugar** — qualquer operação que "parece" modificar uma string na verdade cria uma nova:

```python
linguagem = "Python"
linguagem[0] = "J"  # TypeError: 'str' object does not support item assignment
```

---

# Formatação de Strings (f-strings)

Concatenar strings com `+` funciona, mas fica ilegível rapidamente quando há muitas variáveis misturadas com texto:

```python
"Olá, " + nome + "! Você tem " + str(idade) + " anos e sua nota é " + str(round(nota, 2)) + "."
```

As linguagens modernas resolveram esse problema com uma sintaxe dedicada para **interpolar** variáveis diretamente dentro do texto.

## f-strings em Python

Introduzidas no Python 3.6, as f-strings permitem embutir expressões diretamente dentro de chaves `{}` numa string prefixada com `f`, sendo hoje o método recomendado para formatação de texto em Python — mais rápido e mais legível que `.format()` ou o operador `%` antigo.

```python
nome = "Ana"
idade = 25
nota = 8.756

print(f"Olá, {nome}! Você tem {idade} anos e sua nota é {nota:.2f}.")
# Olá, Ana! Você tem 25 anos e sua nota é 8.76.
```

O `:.2f` dentro das chaves é um especificador de formato — nesse caso, "arredonde para 2 casas decimais".

## Template literals em TypeScript

TypeScript (herdando do JavaScript) tem seu equivalente direto: **template literals**, delimitados por crase (```) em vez de aspas, com `${}` no lugar de `{}`.

```tsx
const nome = "Ana";
const idade = 25;
const nota = 8.756;

console.log(`Olá, ${nome}! Você tem ${idade} anos e sua nota é ${nota.toFixed(2)}.`);
// Olá, Ana! Você tem 25 anos e sua nota é 8.76.
```

## Comparando os métodos de formatação (Python)

| Método | Sintaxe | Recomendação |
| --- | --- | --- |
| `%` (antigo, estilo C) | `"Olá, %s" % nome` | Evitar — mantido só por compatibilidade com código legado |
| `.format()` | `"Olá, {}".format(nome)` | Útil para templates reutilizáveis ou strings vindas de fora do código |
| f-string | `f"Olá, {nome}"` | Recomendado para a grande maioria dos casos — mais legível e mais rápido |

--- 

# Controle de fluxo
## if / else / else if

```tsx
const idade = 20;

if (idade >= 18) {
  console.log("Maior de idade");
} else if (idade >= 12) {
  console.log("Adolescente");
} else {
  console.log("Criança");
}
```

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")
```

```
           idade >= 18? ──sim──▶ "Maior de idade"
                │não
                ▼
        idade >= 12? ──sim──▶ "Adolescente"
                │não
                ▼
           "Criança"
```

## switch (e o equivalente em Python)

Quando há muitas comparações do mesmo valor contra opções diferentes, `switch` organiza melhor do que uma cadeia longa de `else if`:

```tsx
switch (diaDaSemana) {
  case 1:
    console.log("Segunda-feira");
    break;
  case 2:
    console.log("Terça-feira");
    break;
  default:
    console.log("Outro dia");
}
```

```python
# Python não tem "switch" tradicional; desde a versão 3.10 existe "match":
match dia_da_semana:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case _:
        print("Outro dia")
```

> Importante: em TypeScript, esquecer o `break` faz a execução "cair" para o próximo `case` (*fallthrough*) — uma das armadilhas mais citadas sobre `switch`. O `match` do Python não sofre desse problema.
>

---

# Estruturas de repetição

## for

Usado quando sabemos, de antemão, quantas vezes (ou sobre qual coleção) queremos repetir:

```tsx
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

```python
for i in range(5):
    print(i)
```

```
i=0 → executa → i=1 → executa → i=2 → executa → i=3 → executa → i=4 → executa → para (i=5 falha na condição)
```

## while

Usado quando não sabemos, de antemão, quantas vezes será necessário repetir — apenas sabemos a condição que deve permanecer verdadeira:

```tsx
let tentativas = 0;
while (tentativas < 3) {
  console.log(`Tentativa ${tentativas + 1}`);
  tentativas++;
}
```

```python
tentativas = 0
while tentativas < 3:
    print(f"Tentativa {tentativas + 1}")
    tentativas += 1
```

## do-while

Executa o bloco **pelo menos uma vez**, verificando a condição só depois — útil quando a ação precisa acontecer antes de qualquer checagem (ex.: pedir uma senha pelo menos uma vez, mesmo sem saber ainda se está certa):

```tsx
let senha: string;
do {
  senha = "1234"; // simulando uma leitura de entrada
} while (senha !== "correta");
```

```python
# Python não tem "do-while" nativo — o padrão idiomático simula com while True + break:
while True:
    senha = "1234"  # simulando uma leitura de entrada
    if senha == "correta":
        break
```

## Comparando as três estruturas

| Estrutura | Quando usar | Garante ao menos uma execução? |
| --- | --- | --- |
| `for` | Número de repetições conhecido, ou percorrendo uma coleção | Não |
| `while` | Condição conhecida, número de repetições desconhecido | Não |
| `do-while` | Mesma lógica do `while`, mas a ação precisa acontecer ao menos uma vez | Sim |

## O perigo do laço infinito

Um `while` cuja condição nunca se torna falsa nunca termina — trava o programa. Sempre garanta que algo dentro do laço, a cada repetição, aproxima a condição de se tornar falsa (como `tentativas++` no exemplo acima).

---

# Controle de Laços
Nem sempre um laço deve rodar até sua condição natural de parada. Às vezes precisamos interromper mais cedo, ou pular só uma repetição específica, sem quebrar todo o laço.

## break — interrompe o laço por completo

```tsx
for (let i = 0; i < 10; i++) {
  if (i === 5) break;
  console.log(i); // imprime 0, 1, 2, 3, 4
}
```

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # imprime 0, 1, 2, 3, 4
```

## continue — pula para a próxima repetição

```tsx
for (let i = 0; i < 5; i++) {
  if (i === 2) continue;
  console.log(i); // imprime 0, 1, 3, 4 (pula o 2)
}
```

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # imprime 0, 1, 3, 4 (pula o 2)
```

## pass (exclusivo do Python) — não faz nada

Python exige que todo bloco (`if`, `for`, função, etc.) tenha pelo menos uma linha dentro dele — `pass` existe para preencher esse espaço quando, propositalmente, ainda não há nada a fazer ali:

```python
for i in range(5):
    if i == 2:
        pass  # ainda não decidi o que fazer aqui — mas o código precisa ser válido
    print(i)
```

TypeScript não precisa de um equivalente, porque blocos vazios `{}` já são sintaticamente válidos.

## Resumo dos três controles

| Palavra-chave | Efeito |
| --- | --- |
| `break` | Encerra o laço imediatamente, por completo |
| `continue` | Pula apenas a repetição atual, o laço continua |
| `pass` (Python) | Não faz nada — apenas preenche um bloco obrigatório |

---
# Resumo Geral

| Conceito | Ideia principal |
| --- | --- |
| Variável | Espaço nomeado na memória que guarda um valor |
| Tipos primitivos | Classificação de valores (número, texto, booleano...) que define seu comportamento |
| Operadores | Símbolos que combinam ou comparam valores (aritméticos, relacionais, lógicos) |
| Entrada e Saída | Comunicação do programa com o mundo exterior |
| Conversão de tipos | Transformar um valor de um tipo para outro, explícita ou implicitamente |
| Expressão | Combinação de valores e operadores que produz um resultado |
| Strings | Sequência imutável de caracteres |
| f-strings / template literals | Forma moderna e legível de interpolar variáveis em texto |
| Controle de fluxo | Desviar a execução com base em condições (`if`/`switch`) |
| Estruturas de repetição | Executar um bloco várias vezes (`for`/`while`/`do-while`) |
| Controle de laços | Ajustar o comportamento de um laço em andamento (`break`/`continue`/`pass`) |