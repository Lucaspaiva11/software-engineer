# Exercicio 2 - Leia altura e peso de uma pessoa e calcule o IMC.

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura**2) 
print("Seu IMC é: ",imc)