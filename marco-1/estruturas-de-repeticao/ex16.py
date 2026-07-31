# Exercício 16 - Implemente uma busca linear em uma lista de produtos

produtos = [
    'tv','celular','relogio','tablet','smartphone'
]

entrada = input('Digite o nome do produto: ')

for produto in produtos:
    print(produto)
    if entrada == produto:
        print('Produto encontrado')
        break
else:
    print('Produto não existe')