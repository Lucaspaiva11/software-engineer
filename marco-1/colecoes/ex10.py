# Exercicio 10 - Implemente um cadastro de alunos usando uma lista de dicionários
alunos = []
opcao = 'sim'

while opcao == 'sim':
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    ra = int(input('Digite o seu RA: '))


    aluno = dict(nome=nome,idade=idade,ra=ra)
    # Outra forma 
    # aluno = {
    #       "nome":nome,
    #       "idade":idade,
    #       "ra":ra,
    # }

    # print(aluno)
    alunos.append(aluno)
    opcao = input('Deseja cadastrar outro aluno?: ')

print(alunos)