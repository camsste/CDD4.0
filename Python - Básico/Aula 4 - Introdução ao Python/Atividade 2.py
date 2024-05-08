# Fazendo uma programa para fazer a contagem de 0 até o número que o usuário digitar usando "for"

numero = int(input("Digite o número: "))

if numero>0:
    for n in range(0,numero+1,+1):
        print(f"{n}")

else:
    print(f"Insira um novo valor: ")