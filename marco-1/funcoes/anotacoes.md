# Introdução á funções 

## O que é uma Função?

> **Uma função é um bloco de código reutilizável que realiza uma tarefa específica.**
> 

Ela recebe um nome.

Sempre que esse nome é chamado, o computador executa aquele bloco.

---

## Por que funções existem?

Elas permitem:

- reutilizar código;
- dividir problemas grandes;
- organizar programas;
- facilitar testes;
- facilitar manutenção.

---

## Estrutura de uma função

```python
def cumprimentar():
    print("Olá!")
```

| Parte | Significado |
| --- | --- |
| `def` | "Estou definindo uma função" |
| `cumprimentar` | Nome da função |
| `()` | Onde entram parâmetros (Parte 2) |
| `:` | Início do bloco |
| `print("Olá!")` | Corpo da função |

---

## Parâmetro × argumento

> **Parâmetro** é a variável declarada na definição da função. **Argumento** é o valor enviado quando a chamamos.
> 

```python
def cumprimentar(nome):     # "nome" é o parâmetro
    print("Olá", nome)

cumprimentar("Lucas")       # "Lucas" é o argumento
```
## Múltiplos parâmetros e ordem

```python
def apresentar(nome, idade):
    print(nome, idade)

apresentar("Lucas", 21)  # Lucas 21
apresentar(21, "Lucas")  # 21 Lucas
```

Os argumentos são associados aos parâmetros **pela posição**.

---

## Escopo
> **Escopo** é a região do programa onde uma variável existe e pode ser acessada.
> 

## Variáveis locais

```python
def saudacao():
    nome = "Lucas"
    print(nome)

saudacao()
print(nome)  # NameError — "nome" não existe fora da função
```

A variável `nome` existe **apenas** dentro da função; ao terminar, é destruída.

## Variáveis globais

```python
empresa = "OpenAI"

def mostrar():
    print(empresa)

mostrar()  # OpenAI
```

---
## Modularização
> **Modularização** é dividir um programa em pequenas partes independentes, cada uma resolvendo apenas um problema.
>

## Exemplo ruim × melhor

```python
def sistema():
    ler_dados()
    validar()
    calcular()
    salvar()
    enviar_email()
    imprimir_relatorio()
    gerar_pdf()
    # faz praticamente tudo
```

```python
def ler_dados(): ...
def validar(): ...
def calcular(): ...
def salvar(): ...
def enviar_email(): ...
    # cada função possui uma única tarefa
```
---

##  Princípio da Responsabilidade Única (SRP)

> Uma função deve possuir **apenas um motivo para mudar** — ou seja, deve fazer apenas uma coisa.
> 

Um teste rápido: consigo explicar esta função usando apenas **um verbo**? (`Calcular`, `Salvar`, `Buscar`, `Validar`, `Ordenar` — ótimo. Se precisar de cinco verbos diferentes, provavelmente ela deveria ser dividida.)

##  Docstrings

Uma docstring documenta o propósito da função logo abaixo de sua definição — o que ela faz, quais parâmetros recebe, o que retorna:

```python
def dividir(a, b):
    """
    Divide dois números.

    Parâmetros:
        a: dividendo
        b: divisor

    Retorna:
        Resultado da divisão.
    """
```

Pode ser consultada com `help(dividir)`.

##  Organização de arquivos

Programas pequenos cabem em um único `main.py`. Programas maiores se beneficiam de separar por assunto:

```
projeto/
├── main.py
├── usuarios.py
├── calculos.py
├── relatorios.py
└── util.py
```

Pergunta-guia: *essas funções tratam do mesmo assunto?* Se não, provavelmente pertencem a módulos diferentes.

---
## Boas práticas

- Cada função deve ter apenas **uma responsabilidade**
- Use nomes claros e descritivos, de preferência um verbo por função
- Prefira `return` para produzir resultados; `print` só para exibição
- Prefira variáveis locais e parâmetros/`return` em vez de `global`
- Documente funções públicas com docstrings
- Divida arquivos por assunto quando o programa crescer
- Leia o traceback antes de alterar o código

---
## Resumo geral

| Conceito | Definição |
| --- | --- |
| Função | Bloco reutilizável de código |
| Definição | Criação da função |
| Chamada | Execução da função |
| Parâmetro | Variável declarada na função |
| Argumento | Valor enviado na chamada |
| `return` | Devolve um valor ao programa |
| `print` | Exibe informações na tela |
| Escopo | Região onde uma variável existe |
| Variável local | Existe apenas dentro da função |
| Variável global | Existe durante toda a execução do programa |
| Call Stack | Pilha que controla chamadas de funções (LIFO) |
| Traceback | Relatório da sequência de chamadas que levou a um erro |
| Modularização | Dividir um programa em pequenas partes independentes |
| SRP | Uma função deve fazer apenas uma coisa |
| Docstring | Documentação incorporada à função |
| Recursão | Função que chama a si própria |
| Refatoração | Melhorar a estrutura do código sem alterar seu comportamento |