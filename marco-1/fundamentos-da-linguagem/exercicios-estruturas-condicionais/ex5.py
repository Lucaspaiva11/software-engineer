# Exercicio 5 - Determine a categoria de idade: Criança, adolescente, Adulto, Idoso

idade = int(input('Digite sua idade: '))

if idade <= 11:
    print('Criança')
elif idade <= 18:
    print('Adolescente')
elif idade < 59:
    print("Adulto")
else:
    print('Idoso')