# Exercicio 3 - Trate um ValueError ao converter uma entrada para inteiro, e um ZeroDivisionError

try:
    idade = int(input('Digite sua idade: '))
    div = 10 / idade
    print(f'idade: {idade}')
except ValueError:
    print('Só números são permitidos.')
except ZeroDivisionError:
    print('Não existe divisão por Zero!')