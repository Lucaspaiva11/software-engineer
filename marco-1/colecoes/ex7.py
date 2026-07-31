# Exercício 7 - Crie uma lista de notas e imprima sua quantidade com len(); peça um índice ao usuário e valide antes de acessa

notas = [10,8.5,6,6.75,5]
print(len(notas))

indice = int(input('Escolha um índice: '))

if indice <= len(notas)-1:
    print(notas[indice])
else:
    print('Indice não existe')