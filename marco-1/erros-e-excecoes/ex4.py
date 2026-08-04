# Exercicio 4 - Adicionar ELSE e Raise no programa do exercicio 3
class IdadeInvalidaError(Exception):
    pass

try:
    idade = int(input('Digite sua idade: '))
    div = 10 / idade
    if idade < 0:
        raise IdadeInvalidaError("Idades não podem ser negativas")
except ValueError:
    print('Apenas números são permitidos')
except ZeroDivisionError:
    print('Não existe divisão por Zero!')
else:
    print(f'Idade: {idade}')