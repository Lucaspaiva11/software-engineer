# Exercicio 5 - Conte quantos números pares existem entre 1 e 200.

contador = 2
pares = 0

while contador <= 200:
    if contador % 2 == 0:
        pares += 1
    contador += 1
print(f'Existem {pares} números pares')