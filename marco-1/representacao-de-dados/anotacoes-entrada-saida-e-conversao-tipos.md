# Entrada, Saída e Conversão de tipos

# Saída de Dados
A forma mais simples de produzir saída é usando a Função `print()`(Aceitos qualquer tipo)

```python
print("Olá Mundo")
# Olá mundo
```
---
# Entrada de Dados
Função `input()`(Retorna sempre string) recebe as informações digitadas pelo usuário.

```python
nome = input("Digite seu nome: ")
```
---
# Conversão de Tipos
Funções `int()`, `float()` e `str()`para realizar a conversão explicitamente

```python
#Converte para inteiro
idade = int(input("Idade: "))

#Converte para float
preco = float(input("Preco: "))

#Converte para string
numero = 10
texto = str(numero)
```

---
# Boas práticas

- Sempre saiba qual tipo você espera receber.
- Converta os dados o mais próximo possível da entrada.
- Escolha a função de conversão adequada (`int`, `float`, `str`).
- Não assuma que o usuário fornecerá dados válidos.
- Leia cuidadosamente a mensagem da exceção antes de tentar corrigir o problema; o material **Debugging** reforça que compreender a mensagem de erro é o primeiro passo para uma depuração eficiente.

#  Resumo

| Conceito | Definição |
| --- | --- |
| `print()` | Exibe informações ao usuário |
| `input()` | Recebe dados digitados pelo usuário |
| Conversão de tipos | Transformação explícita de um valor para outro tipo |
| `int()` | Converte para inteiro |
| `float()` | Converte para ponto flutuante |
| `str()` | Converte para texto |
| `TypeError` | Operação realizada entre tipos incompatíveis |
| `ValueError` | Valor inadequado para a conversão solicitada |