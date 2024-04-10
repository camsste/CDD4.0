# Fazendo um programa que identifique caso o usuário escreva um número negativo na sequência usando "for"

soma = 0
for x in range(10):

    print(f" valor da soma: {soma} no passo {x}")
    num = int(input("Digite um número: "))
    if num < 0:
        print(f" Achei um número negativo")
        soma = soma + 1
