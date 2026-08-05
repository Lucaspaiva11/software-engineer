# Pensamento Computacional
---
**Programar é resolver problemas, Linguagens são apenas ferramentas.**

**Pensamento Computacional** é a habilidade de resolver problemas complexos aplicando quatro processos, nesta ordem lógica:

```
Problema complexo
   → Decomposição      (divido em partes menores)
   → Reconhecimento de Padrões  (o que já vi parecido antes?)
   → Abstração         (o que importa? o que posso ignorar?)
   → Algoritmo         (quais passos resolvem isso?)
```
---

## Decomposição
Dividir o problema grande em problemas menores que possam ser resolvidos individualmente.
Organizar para diminuir a complexidade!

**Praticamente todo software profissional é desenvolvido dessa forma**

**Quando se deparar com um problema que parece impossível deve se perguntar:**
> "Qual a menor parte do problema que eu consigo resolver agora?"

### Exemplo: "Criar um sistema de cadastro de usuários"

```
Sistema de cadastro
 ├─ Receber dados do formulário
 ├─ Validar os dados (email válido? senha forte?)
 ├─ Verificar se o usuário já existe
 ├─ Salvar no banco de dados
 └─ Enviar e-mail de confirmação
```

Cada um desses cinco itens é um problema pequeno o bastante para ser implementado (e testado) isoladamente — e é exatamente assim que sistemas profissionais são construídos.
---
## Reconhecimento de padrões

> O reconhecimento de padrões é procurar padrões nos problemas e determinar se algo que já encontramos no passado se aplica ao cenário atual
>

**COMO RECONHECER PADRÕES?**
1. repetição de uma mesma operação (percorrer uma lista)
2. semelhança estrutural entre problemas diferentes (buscar um livro numa estante e buscar uma palavra num dicionário são, estruturalmente, o mesmo problema)
3. egularidades nos dados (todo pedido de compra tem cliente, produto e valor)

---
## Abstração
Ignorar detalhes desnecessários e focar no que realmente importa para resolver o problema atual.

**Na programação**

Quando utilizamos:

```
print("Olá")
```

Não precisamos conhecer como o sistema operacional envia caracteres ao terminal.

Esse detalhe foi abstraído.

## Decomposição VS Abstração

| Decomposição | Abstração |
| --- | --- |
| Divide um problema | Esconde detalhes |
| Reduz complexidade | Reduz informação |
| Atua horizontalmente | Atua verticalmente |
| Cria pequenas tarefas | Simplifica cada tarefa |

---
## Algoritmos

> Algoritmo é um sequência finita e bem definida de passos que processam entradas e retornam uma saída
>

Um **algoritmo** é uma sequência finita e bem definida de passos para resolver um problema ou realizar uma tarefa. Três propriedades são obrigatórias:

- **Finitude** — o algoritmo precisa terminar em algum momento, não pode rodar para sempre.
- **Precisão** — cada passo deve ser inequívoco, sem margem para interpretação.
- **Entrada e saída** — recebe dados de entrada (podendo ser nenhum) e produz uma saída.

```
Entrada → [ Passo 1 → Passo 2 → ... → Passo N ] → Saída
```
---
## Pseudocódigo
> **Pseudocódigo** é uma forma de escrever algoritmos usando estrutura de programação, mas com linguagem próxima do português (ou inglês), sem se preocupar com a sintaxe exata de nenhuma linguagem específica.
>
### Convenções comuns de pseudocódigo

```
INÍCIO
  LEIA idade
  SE idade >= 18 ENTÃO
    ESCREVA "Maior de idade"
  SENÃO
    ESCREVA "Menor de idade"
  FIM SE
FIM
```

---
## Fluxogramas

> Um fluxograma representa um algoritmo como um diagrama de formas conectadas por setas, mostrando o caminho que a execução percorre.
>

### Símbolos básicos

```
   ┌───────────┐
   │  Início   │   ← óvalo: início ou fim
   └─────┬─────┘
         ▼
   ┌───────────┐
   │  Leia N   │   ← paralelogramo: entrada/saída
   └─────┬─────┘
         ▼
      ◇ N > 0? ◇   ← losango: decisão
      │        │
     sim      não
      ▼        ▼
 ┌────────┐  ┌────────┐
 │Positivo│  │Negativo│  ← retângulo: processo/ação
 └───┬────┘  └───┬────┘
     └────┬───────┘
          ▼
      ┌───────┐
      │  Fim  │
      └───────┘
```

- **Óvalo** → início e fim do fluxo
- **Retângulo** → uma ação ou processamento
- **Losango** → uma decisão (o fluxo se bifurca)
- **Paralelogramo** → entrada ou saída de dados
- **Setas** → a ordem em que os passos acontecem

---
## Estratégias de Resolução de problemas

### Estratégias práticas

**1. Entenda o problema antes de tentar resolvê-lo.** Reformule o problema com suas próprias palavras. Se você não consegue explicar o problema, ainda não o entendeu o suficiente para resolvê-lo.

**2. Resolva um caso simples primeiro.** Antes de resolver o problema geral, resolva-o para o menor caso possível (um elemento, uma lista vazia, o número zero). Muitas vezes a solução do caso simples revela o padrão da solução geral.

**3. Trabalhe de trás para frente.** Parta do resultado desejado e pergunte: *o que precisa ser verdade imediatamente antes deste resultado?* Repita até chegar ao ponto de partida.

**4. Procure um problema parecido já resolvido.** Isso é reconhecimento de padrões (Capítulo 4) aplicado deliberadamente: "isso se parece com algo que eu já vi?"

**5. Divida e ataque separadamente.** Isso é decomposição (Capítulo 3) aplicada deliberadamente quando o problema parece grande demais.

**6. Explique o problema em voz alta para outra pessoa (ou para um pato de borracha).** O simples ato de verbalizar o raciocínio, passo a passo, frequentemente revela onde está a falha.

---
## Como ler documentação técnica

> Nenhum programador memoriza todas as funções de todas as bibliotecas que usa. A habilidade real, praticada todos os dias no mercado, é **saber procurar e ler documentação oficial** com rapidez e autonomia.
>

### Tipos de documentação técnica

| Tipo | Objetivo | Quando usar |
| --- | --- | --- |
| Tutorial / Getting Started | Ensinar o básico passo a passo | Primeiro contato com a ferramenta |
| Referência (API Reference) | Descrever cada função, parâmetro e retorno | Quando você já sabe o que precisa, só falta o "como" exato |
| Guia (How-to) | Resolver uma tarefa específica | Quando você tem um objetivo prático concreto |

### Como ler documentação com eficiência

1. **Comece pela visão geral.** Antes de mergulhar em detalhes, leia o resumo/overview para entender o propósito geral da ferramenta.
2. **Use a busca, não a leitura linear.** Diferente de um livro, documentação técnica é feita para consulta pontual — busque a palavra-chave relevante em vez de tentar lembrar onde um tópico foi discutido.
3. **Preste atenção aos exemplos de código antes do texto.** Um exemplo de requisição e resposta reais frequentemente esclarece mais rápido do que um parágrafo de explicação.
4. **Observe os diagramas quando existirem** — um diagrama bem feito transmite informação que o texto sozinho não consegue, e vale a pena ser observado antes do texto ao redor.
5. **Assuma que há lacunas.** É comum a documentação pressupor conhecimento prévio que não é dito explicitamente, se algo não fizer sentido, isso não significa necessariamente que você é o problema.

---
## Resumo geral

| Conceito | Ideia principal |
| --- | --- |
| Programar | Descrever passos precisos para que um computador resolva um problema |
| Pensamento Computacional | Decomposição + Reconhecimento de Padrões + Abstração + Algoritmo |
| Decomposição | Dividir um problema grande em partes menores e gerenciáveis |
| Reconhecimento de Padrões | Identificar semelhanças com problemas já resolvidos |
| Abstração | Manter só os detalhes relevantes, ignorar o resto |
| Algoritmo | Sequência finita e precisa de passos, com entrada e saída |
| Pseudocódigo | Algoritmo escrito em linguagem próxima do natural, sem sintaxe rígida |
| Fluxograma | Representação visual de um algoritmo através de formas e setas |
| Estratégias de resolução | Técnicas estruturadas para destravar diante de um problema difícil |
| Documentação técnica | Fonte primária de consulta: tutoriais, referência e guias práticos |