nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
nota3 = float(input("Digite nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Você está aprovado! ;)")
if media <= 4:
    print("Você está reprovado! :(")
else:
    print("Você está de recuperação! :/")

