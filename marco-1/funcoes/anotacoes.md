# Introdução á funções 

## O que é uma Função?

> **Uma **função** é um bloco de código nomeado, reutilizável, que recebe entradas (opcionais), executa uma lógica definida uma única vez no código-fonte, e opcionalmente devolve um resultado.**
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
---
## Valores padrão
Muitas vezes um argumento tem um valor "mais comum", e só ocasionalmente precisa ser diferente. Em vez de exigir que todo chamador informe esse valor sempre, podemos definir um **valor padrão**.

## Definindo valores padrão

```tsx
function criarConta(nome: string, saldoInicial: number = 0): string {
  return `Conta de ${nome} criada com saldo de R$ ${saldoInicial}`;
}

console.log(criarConta("Ana"));         // saldoInicial assume 0
console.log(criarConta("Ana", 500));    // saldoInicial vira 500
```

```python
def criar_conta(nome, saldo_inicial=0):
    return f"Conta de {nome} criada com saldo de R$ {saldo_inicial}"

print(criar_conta("Ana"))         # saldo_inicial assume 0
print(criar_conta("Ana", 500))    # saldo_inicial vira 500
```
---

## Múltiplos parâmetros e ordem

```python
def apresentar(nome, idade):
    print(nome, idade)

apresentar("Lucas", 21)  # Lucas 21
apresentar(21, "Lucas")  # 21 Lucas
```

Os argumentos são associados aos parâmetros **pela posição**.

---

## Argumentos posicionais ou nomeados
Quando uma função tem muitos parâmetros, chamar `criarUsuario("Ana", 25, "ana@email.com", true, false)` obriga quem lê o código a decorar a ordem exata de cada valor. Argumentos nomeados resolvem esse problema.

## Argumentos posicionais

A forma que já usamos até aqui: o valor é associado ao parâmetro pela **posição** em que aparece na chamada.

```python
def criar_usuario(nome, idade, email):
    print(f"{nome}, {idade} anos, {email}")

criar_usuario("Ana", 25, "ana@email.com")  # posicional — a ordem importa
```

## Argumentos nomeados (keyword arguments)

Python permite nomear explicitamente cada argumento na chamada, tornando a ordem irrelevante e o código autoexplicativo:

```python
criar_usuario(email="ana@email.com", nome="Ana", idade=25)  # a ordem não importa mais
```
## Comparando as duas formas

| Característica | Posicional | Nomeado |
| --- | --- | --- |
| Ordem importa? | Sim | Não |
| Legibilidade na chamada | Menor, em funções com muitos parâmetros | Maior — cada valor se explica |
| Risco de erro | Trocar a ordem de dois parâmetros do mesmo tipo | Praticamente nenhum |
---

## Retorno
Uma função pode simplesmente *fazer* algo (imprimir uma mensagem) ou *calcular e devolver* um valor para ser usado em outro lugar do programa. A palavra-chave `return` é o que torna esse segundo caso possível.

## return: devolvendo um valor

```python
def dobrar(numero):
    return numero * 2

resultado = dobrar(5)  # 10
```

Assim que `return` executa, a função é encerrada imediatamente — nenhuma linha depois dele, dentro da mesma função, é executada.

## Funções sem retorno explícito
```python
def logar(mensagem):
    print(mensagem)  # não há "return" — a função retorna None implicitamente

resultado = logar("oi")
print(resultado)  # None
```
---

## Escopo
> **Escopo** é a região do programa onde uma variável existe e pode ser acessada.
> 

## Escopo local × escopo global
```python
contador = 0  # escopo global

def incrementar():
    local = 10  # escopo local
    global contador  # necessário em Python para modificar uma variável global de dentro da função
    contador += 1

incrementar()
print(contador)  # 1
print(local)     # NameError: name 'local' is not defined
```

> Importante: em Python, tentar apenas **reatribuir** uma variável global de dentro de uma função sem a palavra-chave `global` cria, silenciosamente, uma nova variável local com o mesmo nome — uma armadilha muito comum para quem está começando.
>
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

---
## `args`
E se você não souber, de antemão, quantos argumentos uma função vai receber? Uma função de soma deveria funcionar tanto para 2 números quanto para 10.

## args em Python

O prefixo `*` antes de um parâmetro coleta **qualquer quantidade** de argumentos posicionais numa tupla:

```python
def somar(*numeros):
    return sum(numeros)

print(somar(1, 2))          # 3
print(somar(1, 2, 3, 4, 5)) # 15
```
---
## `*kwargs`

Assim como `*args` resolve "número variável de argumentos posicionais", às vezes precisamos de "número variável de argumentos **nomeados**" — sem saber de antemão quais nomes de configuração serão passados.

## *kwargs em Python

O prefixo `**` coleta qualquer quantidade de argumentos nomeados num dicionário:

```python
def criar_perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

criar_perfil(nome="Ana", idade=25, cidade="São Paulo")
# nome: Ana
# idade: 25
# cidade: São Paulo
```
##  `args` × `*kwargs`

|  | `*args` | `**kwargs` |
| --- | --- | --- |
| Coleta | Argumentos posicionais | Argumentos nomeados |
| Estrutura resultante | Tupla | Dicionário |
---

## Efeito colateral

Um **efeito colateral** ocorre quando um função modifica um estado externo a ela (uma variável global, uma propriedade de um objeto, um arquivo em disco, o próprio console) ou depende de um estado externo que pode mudar entre chamadas.

```python
total = 0

def adicionar_ao_total(valor):
    global total
    total += valor  # efeito colateral
    return total
```
### Por que efeitos colaterais tornam o código menos previsível?

Chamar `adicionarAoTotal(5)` duas vezes seguidas produz **resultados diferentes** (5, depois 10) mesmo passando o mesmo argumento — porque o resultado depende de um estado escondido (`total`) que muda a cada chamada. Isso dificulta testar a função isoladamente (Parte 9) e dificulta prever o comportamento do programa só de ler o código.

> Efeitos colaterais não são "errados" — programas reais precisam interagir com o mundo (gravar em banco de dados, exibir na tela, fazer chamadas de rede). O problema é espalhá-los por toda a lógica de negócio sem controle, misturados com cálculos que poderiam ser previsíveis.
>

---

## Funções Puras

Uma função é **pura** quando satisfaz duas condições: (1) para a mesma entrada, sempre produz a mesma saída; e (2) não causa nenhum efeito colateral observável.

```python
def somar(a, b):
    return a + b  # pura: mesma entrada, sempre a mesma saída, sem efeitos colaterais
```

## Pura × Impura

| Característica | Função Pura | Função Impura |
| --- | --- | --- |
| Depende de estado externo? | Não | Frequentemente sim |
| Modifica algo fora dela? | Não | Frequentemente sim |
| Previsibilidade | Alta — sempre o mesmo resultado | Baixa — pode variar entre chamadas |
| Facilidade de testar | Alta | Baixa (exige simular o estado externo) |
| Segurança em execução concorrente | Alta | Baixa, sem cuidados extras |

## Nem tudo pode ser puro

Um programa inteiramente puro não interage com o mundo (não grava nada, não exibe nada, não faz chamadas de rede) — o que na prática é inútil. A prática recomendada não é "eliminar toda impureza", mas **isolar** as partes impuras (I/O, banco de dados, rede) das partes que fazem cálculo e lógica de negócio, mantendo essas últimas o mais puras possível.

---

## Organização de Código
Ter funções não é suficiente se todas elas fizerem "um pouco de tudo". Uma função de 200 linhas que valida dados, calcula um total, salva no banco e envia um e-mail é tecnicamente uma função, mas na prática é tão difícil de entender e testar quanto um bloco de código sem nenhuma função.

## Responsabilidade única

Cada função deveria fazer **uma coisa bem definida**, e seu nome deveria descrever exatamente essa coisa. Se você precisa usar "e" para descrever o que uma função faz ("valida o email **e** salva no banco **e** envia um e-mail"), ela provavelmente deveria ser dividida em funções menores.

```python
def validar_dados(dados):
    ...
    return True

def salvar_usuario(dados):
    ...

def enviar_email_boas_vindas(email):
    ...

def processar_cadastro(dados):
    if not validar_dados(dados):
        return
    salvar_usuario(dados)
    enviar_email_boas_vindas(dados["email"])
```
Note como `processarCadastro` continua existindo, mas agora ela **orquestra** funções menores em vez de fazer tudo sozinha, cada uma das funções menores pode ser lida, testada e reutilizada isoladamente.

## Funções pequenas, nomes descritivos

Uma função pequena o suficiente para caber inteira na tela, com um nome que descreve exatamente o que ela faz, praticamente elimina a necessidade de comentários explicativos.

---

## Recursão (Introdução)

**Recursão** é uma técnica em que uma função resolve um problema chamando a si mesma para resolver uma versão menor do mesmo problema, até atingir um **caso base** — uma versão do problema simples o suficiente para ser resolvida diretamente, sem mais chamadas.

```python
def fatorial(n):
    if n == 0:
        return 1               # caso base
    return n * fatorial(n - 1)  # chamada recursiva

print(fatorial(5))  # 120
```

```
fatorial(5) = 5 * fatorial(4)
                    = 5 * (4 * fatorial(3))
                          = 5 * (4 * (3 * fatorial(2)))
                                = 5 * (4 * (3 * (2 * fatorial(1))))
                                      = 5 * (4 * (3 * (2 * (1 * fatorial(0)))))
                                            = 5 * (4 * (3 * (2 * (1 * 1))))  ← caso base
                                            = 120
```

---

## Resumo geral

| Conceito | Ideia principal |
| --- | --- |
| Função | Bloco nomeado e reutilizável de código |
| Argumento × Parâmetro | Valor passado na chamada × nome usado na definição |
| Valor padrão | Valor assumido quando o argumento não é fornecido |
| Argumentos posicionais/nomeados | Associação por ordem × associação por nome |
| Retorno | Valor devolvido pela função via `return` |
| Escopo | Onde uma variável é visível (local, global, de bloco) |
| `*args` / rest parameters | Número variável de argumentos posicionais |
| `**kwargs` / objeto | Número variável de argumentos nomeados |
| Efeito colateral | Modificação de estado externo à função |
| Função pura | Sem efeitos colaterais, sempre a mesma saída para a mesma entrada |
| Organização de código | Funções pequenas, cada uma com responsabilidade única |
| Recursão | Função que chama a si mesma para um problema menor, até um caso base |