# Pensamento Computacional
---
**Programar é resolver problemas, Linguagens são apenas ferramentas.**

> Algoritmo é um sequência finita e bem definida de passos que processam entradas e retornam uma saída

## Passos para resolver um problema
1. Qual problema preciso resolver? O que o usuário quer?
2. Quais informações entram? (Entradas)
3. O que precisa acontecer? (Processamento)
4. Que resultado deve sair? (Saída)

## Modelo IPO (INPUT-PROCESS-OUTPUT)
```
Entrada -> Processamento -> Saída
```
---
## Como resolver um problema(O verdadeiro trabalho de um programador)?

Programador não fica só escrevendo código!
Em boa parte do seu tempo ele atua em:

1. Entender o problema
2. Pensar
3. Desenhar soluções
4. Testar hipóteses
5. Refinar algoritmos
6. Escreve o código

---

## Técnica/Habilidade importante

### Decomposição
Dividir o problema grande em problemas menores que possam ser resolvidos individualmente.
Organizar para diminuir a complexidade!

## Exemplo

**Problema:**

```
Criar um sistema bancário
```

Muito grande.

Vamos dividir.

```
Sistema Bancário

├── Cadastro de clientes
├── Contas
├── Depósitos
├── Saques
├── Transferências
├── Extrato
└── Login
```

Agora cada parte pode ser resolvida separadamente.

**Praticamente todo software profissional é desenvolvido dessa forma**

**Quando se deparar com um problema que parece impossível deve se perguntar:**
> "Qual a menor parte do problema que eu consigo resolver agora?"

## Exemplo

Sistema de estoque.

Em vez de pensar:

```
Sistema inteiro
```

Pense:

```
Cadastrar produto
```

Depois:

```
Editar produto
```

Depois:

```
Excluir produto
```

Depois:

```
Pesquisar produto
```

Sem perceber, o sistema inteiro estará pronto.

---

## Outra Habilidade importante

### Abstração
Ignorar detalhes desnecessários e focar no que realmente importa para resolver o problema atual.

**Na programação**

Quando utilizamos:

```
print("Olá")
```

Não precisamos conhecer como o sistema operacional envia caracteres ao terminal.

Esse detalhe foi abstraído.

---

## Decomposição VS Abstração

| Decomposição | Abstração |
| --- | --- |
| Divide um problema | Esconde detalhes |
| Reduz complexidade | Reduz informação |
| Atua horizontalmente | Atua verticalmente |
| Cria pequenas tarefas | Simplifica cada tarefa |

---

## Fluxo que sempre deve ser seguido para resolver problemas 

```
Problema

↓

Compreender

↓

Dividir

↓

Eliminar detalhes desnecessários

↓

Criar algoritmo

↓

Implementar

↓

Testar

↓

Melhorar
```

---

## O algoritmo deve vir antes do código

1. Pseudocódigo -> Intermedia entre linguagem humana e linguagem de programação
    Objetivo: Comunicar claramente a lógica

**EXEMPLO:**
```
INÍCIO

Receber nota1

Receber nota2

media ← (nota1 + nota2) / 2

Mostrar media

FIM
```

2. Fluxograma -> Transforma o algoritmo em um diagrama visual
    Objetivo: Visualizar decisões e fluxo de execução antes de implementar

**EXEMPLO:**
```
           ┌──────────┐
           │  Início  │
           └────┬─────┘
                │
                ▼
      ┌───────────────────┐
      │     Ler idade     │
      └─────────┬─────────┘
                │
                ▼
        ┌──────────────┐
        │ idade >= 18? │
        └──────┬───────┘
         Sim   │   Não
          │    │
          ▼    ▼
 ┌────────────┐ ┌────────────────┐
 │ Pode votar │ │ Não pode votar │
 └──────┬─────┘ └──────┬─────────┘
        │              │
        └──────┬───────┘
               ▼
        ┌──────────┐
        │   Fim    │
        └──────────┘
```



