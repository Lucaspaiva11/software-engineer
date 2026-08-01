# Tratamento de Erros e Exceções

Situações como arquivo inexistente, texto onde se esperava numero, divisão por zero ou conexão perdida não são necessariamente defeitos do programa. São acontecimentos que precisam ser tratados.

# Erro
>**Um erro é qualquer sitação que impede um programa de executar como o esperado**
>

# Exceção
>**Uma Exceção é um evento detectado durante a execução que interrompe o fluxo normal do programa**

O Python identifica o problema, interrompe a execução e  informa exatamente o que aconteceu.

### Exemplos comuns de exceções
```python
10 / 0              # ZeroDivisionError — não existe divisão por zero
int("vinte")        # ValueError — não conseguiu converter para inteiro
["Ana"][5]           # IndexError — posição inexistente na lista
{}["nome"]           # KeyError — chave inexistente no dicionário
```
---
# Traceback

Quando uma exceção acontece, o Python mostra um relatório chamado **traceback**, indicando onde o erro ocorreu, em qual arquivo, em qual linha e qual exceção foi lançada:

```
Traceback (most recent call last):
  File "main.py", line 5
ZeroDivisionError: division by zero
```

>  Leia de baixo para cima: a **última linha** normalmente informa qual foi o problema; as linhas anteriores mostram como o programa chegou até ele.
>

## Como investigar (em vez de "adivinhar")

```
1. Leia o nome da exceção
2. Leia a mensagem
3. Descubra a linha indicada
4. Analise os valores envolvidos
5. Corrija a causa do problema
```

## Principais exceções para iniciantes

| Exceção | O que significa |
| --- | --- |
| `TypeError` | Operação entre tipos incompatíveis |
| `ValueError` | Valor inválido para a operação |
| `IndexError` | Índice inexistente em uma sequência |
| `KeyError` | Chave inexistente em um dicionário |
| `NameError` | Variável ou nome não definido |
| `ZeroDivisionError` | Divisão por zero |
| `FileNotFoundError` | Arquivo não encontrado |

---
# `try`,`except`,`else` e `finally`
```
Sem tratamento:  Programa → Erro → Fim
Com tratamento:  Programa → Erro → Resolver problema → Continuar execução
```

## `try` / `except`

```python
try:
    idade = int(input("Idade: "))
    print("Cadastro realizado.")
except ValueError:
    print("Digite apenas números.")
```

Sem o `try`, digitar `"vinte"` encerraria o programa com `ValueError`. Com o tratamento, o programa simplesmente informa o problema e continua.

## Capturando exceções diferentes

```python
try:
    idade = int(input())
    resultado = 10 / idade
except ValueError:
    print("Entrada inválida.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

Também é possível agrupar: `except (ValueError, TypeError):`

---
# `else` — só quando **não** houve erro

```python
try:
    idade = int(input())
except ValueError:
    print("Valor inválido.")
else:
    print("Cadastro realizado.")   # só executa se NADA deu errado
```

---

# `finally` — sempre executa

```python
try:
    print("Abrindo arquivo.")
except:
    print("Erro.")
finally:
    print("Fechando recursos.")   # executa MESMO se houve exceção
```

> Como um restaurante: independentemente de como terminou o jantar, a mesa precisa ser limpa. `finally` representa essa "limpeza obrigatória" — muito usado para fechar arquivos e conexões.
> 

## Estrutura completa

```python
try:
    ...
except ValueError:
    ...
else:
    ...
finally:
    ...
```

Nem todos os blocos são obrigatórios, mas essa é a ordem completa.
---
# `raise`, propagação e exceções personalizadas
Nem todo erro surge automaticamente. Um saque de `-100` não é um erro para o Python — mas é inválido para um sistema bancário. O próprio programa precisa identificar essa situação e interromper a operação: é para isso que existe o `raise`.

> Até agora vimos o Python dizendo *"encontrei um problema"*. Com `raise`, nós dizemos ao Python: *"encontrei um problema — lance esta exceção."*
> 

## Lançando exceções manualmente

```python
idade = -5
if idade < 0:
    raise ValueError("A idade não pode ser negativa.")
```

```python
def sacar(valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser maior que zero.")
    print("Saque realizado.")
```

O Python não conhece regras de negócio como *CPF vazio*, *saldo negativo* ou *pedido sem itens* — quem deve validar isso é o próprio programa.

## Propagação de exceções

Quando uma exceção não é tratada, ela "sobe" pela cadeia de chamadas:

```python
def dividir():
    return 10 / 0

def calcular():
    dividir()

calcular()
# calcular() → dividir() → ZeroDivisionError → volta para calcular()
#    → não foi tratada → o programa encerra
```

>  Pergunta-guia: *esta função sabe resolver o problema?* Se sim, trate a exceção ali mesmo. Se não, deixe-a ser propagada para quem souber.
> 

## Hierarquia de exceções

```
BaseException
    └── Exception
          ├── ValueError
          ├── TypeError
          ├── IndexError
          ├── KeyError
          ├── FileNotFoundError
          └── ...
```

`except Exception:` captura praticamente todas as exceções comuns — mas capturar exceções **específicas** costuma ser mais recomendado.

## Exceções personalizadas

```python
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")
```

Nomes como `ProdutoEsgotadoError`, `PagamentoRecusado` ou `CupomInvalido` comunicam o problema muito melhor do que um genérico `ValueError`.

## Casos reais

```
Saldo insuficiente → SaldoInsuficienteError
Senha inválida → CredenciaisInvalidasError
Usuário inexistente → UsuarioNaoEncontradoError
Produto indisponível → ProdutoEsgotadoError
```

---

# Boas práticas, `assert` e depuração profissional
Comparando dois sistemas: um que encerra tudo diante de um erro, e outro que identifica o problema, exibe uma mensagem adequada e continua funcionando — a diferença de confiança não está na ausência de erros, mas em **como eles são tratados**.

Um bom programador escreve programas que detectam problemas rapidamente, informam o que aconteceu, recuperam-se quando possível, e facilitam a investigação quando algo realmente falha.

## Evite esconder exceções

```python
# Ruim — o erro desaparece, mas o problema continua existindo
try:
    ...
except Exception:
    pass

# Melhor — informa exatamente o que aconteceu
try:
    ...
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

Mensagens úteis fazem diferença: `"Erro."` diz pouco; `'Arquivo "usuarios.txt" não foi encontrado.'` já aponta o caminho da correção.

## `assert`

Usado para verificar condições que **deveriam sempre ser verdadeiras** durante o desenvolvimento — não para validar dados externos:

```python
idade = 20
assert idade >= 0   # condição interna que nunca deveria ser falsa

# se for falsa: AssertionError
```

> Não use `assert` para validar entrada do usuário (`assert idade > 0` num dado vindo de formulário) — para isso, valide explicitamente e lance a exceção apropriada com `raise`.
> 

## Processo profissional de depuração

Depurar é um processo sistemático, não tentativa e erro:

```
Encontrar erro → Reproduzir → Ler traceback → Entender causa
   → Hipótese → Corrigir → Testar novamente → Confirmar solução
```

> Nunca faça: `Erro → alterar dez arquivos → executar → torcer para funcionar`. Prefira uma alteração por vez, testando a cada mudança — isso torna muito mais fácil identificar a causa real.
> 

**Breakpoints** permitem pausar o programa, observar variáveis e acompanhar o fluxo até descobrir exatamente onde o comportamento esperado mudou. Ao inspecionar variáveis, sempre pergunte: *o valor desta variável é realmente o que eu esperava?*

## Casos reais

```
API: requisição falha → resposta HTTP adequada → registro em log
Banco de dados: consulta falha → rollback → mensagem apropriada
Sistema bancário: saldo insuficiente → operação cancelada → conta consistente
```

## Erros comuns (consolidado)

- Ignorar a mensagem da exceção, ou ler só a primeira linha do traceback
- Corrigir o sintoma em vez da causa
- Tentar decorar exceções em vez de aprender a interpretá-las
- Usar `except:` (ou `except Exception:`) sem necessidade, escondendo problemas
- Colocar código demais dentro de um único `try`
- Usar `except: pass` — o erro é escondido, não resolvido, virando um bug difícil de rastrear
- Esquecer o `finally` quando recursos (arquivos, conexões) precisam ser liberados
- Usar `raise` para situações que uma validação simples já evitaria
- Criar exceções personalizadas para qualquer coisa, sem que representem um conceito real do domínio
- Usar `assert` para validar dados externos em vez de hipóteses internas do programa
- Alterar vários arquivos de uma vez ao depurar, em vez de uma mudança por vez


## Boas práticas

- Leia o traceback inteiro antes de alterar qualquer coisa; identifique a causa antes da solução
- Capture exceções específicas sempre que possível; mantenha o `try` pequeno
- Use `else` para o código que só deve rodar se nada deu errado, e `finally` para liberar recursos
- Use `raise` para representar violações de regras de negócio, com mensagens objetivas
- Crie exceções personalizadas quando tornarem o código mais expressivo
- Use `assert` apenas para hipóteses internas; valide entradas externas com `raise`
- Reproduza o erro antes de corrigir, faça uma alteração por vez, e teste novamente após cada correção

---

## Resumo geral

| Conceito | Definição |
| --- | --- |
| Erro | Situação que impede o funcionamento esperado |
| Exceção | Evento detectado durante a execução que interrompe o fluxo normal |
| Traceback | Relatório indicando onde e como a exceção ocorreu |
| `try` | Executa código que pode gerar exceções |
| `except` | Trata exceções |
| `else` | Executa apenas quando não houve erro |
| `finally` | Executa sempre, liberando recursos quando necessário |
| `raise` | Lança uma exceção manualmente |
| Propagação | A exceção sobe pela cadeia de chamadas até ser tratada |
| Hierarquia | Organização das exceções em classes (`Exception` como base comum) |
| Exceção personalizada | Classe criada para representar um erro específico do domínio |
| `assert` | Verifica hipóteses internas que deveriam ser sempre verdadeiras |