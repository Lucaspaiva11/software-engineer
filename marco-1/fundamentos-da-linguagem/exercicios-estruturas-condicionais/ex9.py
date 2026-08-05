# Exercicio 9 - Desenvolva um sistema de cadastro de funcionários:
# administrador, gerente, funcionário e visitante
# Utilize match para identificar o cargo e, dentro de cada caso, aplique condicionais adicionais para verificar permissões específicas.

cargo = input('Informe o seu cargo: ')

match cargo:
    case 'administrador':
        print('Permissões:')
        print('1. Cadastrar funcionarios')
        print('2. Editar funcionarios')
    case 'gerente':
        print('Permissões:')
        print('1. Contratar')
        print('2. Efetivar')
    case 'funcionário':
        print('Permissões:')
        print('1. Bater ponto')
    case 'visitante':
        print('Permissões:')
        print('1. Acessar hall')
    case _:
        print('Cargo inexistente')