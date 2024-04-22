# Crie um algoritmo que leia um número e diga se ele é par ou ímpar e usando While
resposta = 'sim'
while resposta == 'sim' or resposta == 'Sim':
    numero = int(input("Escreva um número para descobrir se ele é par ou ímpar: "))
    if numero % 2 != 0:
        print(f"O número {numero} é ímpar")
    else:
        print(f"O número {numero} é par")

    resposta = str(input("Deseja inserir outro número?"))