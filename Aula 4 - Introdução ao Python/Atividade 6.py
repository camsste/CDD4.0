# Ler 10 valores e calcular a média aritmétrica desses valores lidos usando "While"

soma = 0
b = 0

while b < 10:
    num = float(input(f"Digite a sua nota: "))
    soma = soma + num
    b = b + 1

media = soma / 10
print(f" A sua média aritmétrica é: {media}")


