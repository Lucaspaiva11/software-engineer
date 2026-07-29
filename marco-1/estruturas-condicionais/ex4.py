# Exercicio 4 - Verifique se um usuário pode acessar uma área restrita apenas quando estiver autenticado

senha = '1234'
login = input('Digite a senha da área restrita: ')

if login == senha:
    print('Acesso liberado')
else:
    print('Acesso negado')