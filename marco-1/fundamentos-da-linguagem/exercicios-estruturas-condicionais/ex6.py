# Exercicio 6 - Sistema de cálculo de desconto

valor = float(input('Digite o valor da sua compra: '))

if valor >= 1000:
    valor *= 0.2
    print(f'Desconto de 20%, ${valor}')
elif valor >= 500:
    valor *= 0.1
    print(f'Desconto de 10%, ${valor}')
elif valor >= 200:
    valor *= 0.05
    print(f'Desconto de 5%, ${valor}')
else: 
    print('Sem desconto disponível')