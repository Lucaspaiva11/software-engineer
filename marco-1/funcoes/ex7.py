# Exercicio 7 - Implemente um sistema de vendas dividido em calcular_subtotal, calcular_desconto, calcular_imposto e calcular_valor_final — todas recebendo parâmetros e retornando valores, sem print interno (exceto na função principal)

def calcular_subtotal(preco,quantidade):
    return preco*quantidade
    
def calcular_desconto(subtotal):
    if subtotal >= 500:
        return subtotal * 0.1
    return 0

def calcular_imposto(subtotal):
    return subtotal * 0.15

def calcular_valor_final(subtotal,desconto,imposto):
    return subtotal-desconto+imposto

subtotal = calcular_subtotal(200,4)
desconto = calcular_desconto(subtotal)
imposto = calcular_imposto(subtotal)
valor_final = calcular_valor_final(subtotal,desconto,imposto)

print(valor_final)