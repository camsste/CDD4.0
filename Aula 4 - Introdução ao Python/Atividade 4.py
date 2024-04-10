# Programa que identifica caso o número esteja fora ou dentro da sequencia de 10 à 20 usando "for"

dentro = 0

for x in range(10):

    num = int(input("Digite um número: "))
    if num >= 10 and num <= 20 :
        dentro = dentro + 1
        print(f"Os números que estão dentro são: {dentro}")

    fora = 10 - dentro
    print(f"Os números que estão fora do intervalo são: {fora}")