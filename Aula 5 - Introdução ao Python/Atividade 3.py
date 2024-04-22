# Crie um código que leia a idade de uma pessoa e diga em qual ano ela nasceu
idade = int(input("Insira a sua idade: "))
mes = int(input("Insira o mês de nascimento: "))
ano = 2024 - idade
if mes >= 4:
    ano = ano - 1
    print(ano)
else:
    print(ano)