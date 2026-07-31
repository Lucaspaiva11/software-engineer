# Exercicio 6 - Crie uma função que receba uma lista de números e retorne o maior valor

def retorna_maior(numeros):
    maior = 0
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

print(retorna_maior([12,34,7,84,32,118,22,5,95]))