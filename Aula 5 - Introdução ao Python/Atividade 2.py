# Crie um código que leia um número diferente de zero e diga se este número é positivo ou não adicionando também uma estrutura de repetição ao final do código
resposta = 'sim'

while resposta == 'sim' or resposta == 'Sim':
    num = int(input("Insira um número negativo ou positivo: "))

    if num >= 1:
        print(f"O número é positivo!")
    elif num <= -1:
        print(f"O número é negativo!")
    else:
        print(f"O número é 0")

    resposta = str(input("Deseja refazer? (Sim ou Não): "))