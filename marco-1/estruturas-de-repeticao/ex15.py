# Exercício 15 - Faça um menu com while True e break.

while True:
    print('1.Cadastrar')
    print('2.Alterar')
    print('3.Excluir')
    print('4.Sair')
    sair = input('Escolha uma opção: ')

    if sair == 'Sair' or sair == 'sair':
        break