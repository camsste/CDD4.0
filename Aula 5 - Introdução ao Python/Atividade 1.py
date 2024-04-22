# Crie um código que some duas notas, diga a média e se o aluno está reprovado, aprovado ou em recuperação.
soma = 0

for x in range(2):
    nota = float(input("Insira sua nota: "))
    soma = soma + nota
media = soma/2

if media >= 7:
    print(f"Sua média foi {media}. Você foi aprovado!")
elif media >=4:
    print(f"Sua média {media}. Você está de recuperação!")
else:
    print(f"Sua média {media}. Você foi reprovado!")