# Exercicio 8 - Implemente um sistema de login com: usuário, senha e conta ativa

usuario = 'lucas.paiva'
senha = 'password123'
conta_ativa = True

if usuario == 'lucas.paiva' and senha == 'password123':
    if conta_ativa:
        print('Login efetuado')
    else: 
        print('Conta inativa')
else:
    print('Usuário ou senha incorretos')