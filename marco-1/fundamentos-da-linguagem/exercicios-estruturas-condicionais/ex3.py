# Exercicio 3 - Crie um programa que permita um saque apenas quando o saldo for suficiente

saldo = 1000
saque = 100

if saque <= saldo:
    print(f'Saque concluído! ${saque}')
else:
    print('Saldo insuficiente')