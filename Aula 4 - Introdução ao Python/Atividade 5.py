# Ler 10 valores e calcular a média aritmétrica desses valores lidos usando "for"

soma = 0
for x in range(10):

    num = int(input("Digite um número: "))
    soma = soma + num

media = soma / 10
print(f" A média aritmétrica é: {media}")
