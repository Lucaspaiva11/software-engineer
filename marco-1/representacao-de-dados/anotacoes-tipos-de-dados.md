# Representação de dados

*DADO* -> Valor isolado, ainda sem contexto
*INFORMAÇÃO* -> Dados interpretado dentro de um contexto

> **O computador não entende dado, e o significado dele é responsabilidade do programador**

```
42

Para o PC é apenas um numero inteiro.

idade = 42 

Agora tem um significado
```

Sempre que começar um programa, pergunte:

> **Quais informações preciso representar?**
> 

Depois transforme essas informações em dados.

Exemplo.

Sistema bancário.

Informações:

```
Cliente

Saldo

Conta

PIX
```

Transformação.

```
Nome

Número

Decimal

Texto
```

Agora fica muito mais fácil escolher como armazenar cada informação.

---
# O que é um Tipo?

> **Um tipo define quais características um valor possui e quais operações podem ser realizadas sobre ele.**
>

Um tipo serve para determinar:
- Como o valor será armazenado;
- Quais operações são permitidas;
- Quanto espaço ocupará na memória;
- Como o interpretador deverá tratá-lo

# Principais tipos primitivos

## Inteiro (int)
- Números sem parte decimal
Exemplos:
```
10, 0 , -50
Casos reais:
Idade, quantidade, estoque
```
## Ponto Flutuante (Float)
- Números com parte decimal
Exemplos:
```
3.14, 99.99, -7.5
Casos reais:
Preço, altura, peso, temperatura 
```

## Strings (Str)
- Representam texto (Caracteres)
Exemplos:
```
"Lucas", "Civic", "Corinthians"
Casos reais:
Nome, endereço, senha
```
## Booleanos (Bool)
- Representam dois estados -> **True** ou **False**
```
Casos reais:
Usuário autenticado, pagamento realizado, produto disponível, conta ativa
```

# Comparação
| Tipo | Representa | Exemplos |
| --- | --- | --- |
| int | números inteiros | 10, -5, 0 |
| float | números decimais | 3.14, 8.5 |
| str | texto | "Python", "Lucas" |
| bool | verdadeiro ou falso | True, False |

Escolher tipos adequados torna o programa mais claro e reduz a chance de erros.

# Erros para não cometer

- String não é igual a inteiro
    `"10"` é diferente de `10`

- Usar Float para contar objetos
    `25`Correto | `25.0` Incorreto

- Usar inteiro para representar dinheiro

# Resumo
| Conceito | Definição |
| --- | --- |
| Dado | Valor isolado |
| Informação | Dado com contexto |
| Valor | Unidade básica manipulada pelo programa |
| Tipo | Define como um valor é representado e manipulado |
| int | Inteiros |
| float | Decimais |
| str | Texto |
| bool | Verdadeiro/Falso |