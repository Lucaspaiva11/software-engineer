# Expressões: como os programas produzem novos valores

# Expressões
> **Uma expressão é qualquer combinação de valores, variáveis e operadores que produz um novo valor.**
>

---
# Operadores

Os operadores são símbolos que indicam qual operação deve ser realizada.

# Operadores Aritméticos

| Operador | Significado |
| --- | --- |
| `+` | Soma |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `//` | Divisão inteira |
| `%` | Resto da divisão |
| `**` | Potenciação |

---

# Expressões com variáveis
```
preco=100
desconto=20

# Expressão
preco - desconto -> 100 - 200
```

# Ordem de precedência (introdução)

| Prioridade | Operadores |
| --- | --- |
| 1 | `( )` |
| 2 | `**` |
| 3 | `* / // %` |
| 4 | `+ -` |

---

# Boas práticas

- Utilize parênteses para tornar a intenção explícita, mesmo quando não forem estritamente necessários.
- Escreva expressões pequenas e legíveis.
- Evite repetir cálculos; armazene resultados intermediários em variáveis quando fizer sentido.
- Sempre verifique se uma expressão apenas calcula ou também altera o estado do programa.

#  Resumo

| Conceito | Definição |
| --- | --- |
| Expressão | Combinação de valores, variáveis e operadores que produz um novo valor |
| Operador | Símbolo que indica uma operação |
| Atribuição | Associa o resultado de uma expressão a uma variável |
| Precedência | Regras que definem a ordem de avaliação das operações |
| Estado do programa | Conjunto dos valores das variáveis em um determinado momento |