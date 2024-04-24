branco = int(input("Escreva a quantidade de votos brancos teve na eleição: "))
nulo = int(input("Escreva a quantidade de votos nutos que teve na eleição: "))
validos = int(input("Escreva a quatidade de votos válidos que teve na eleição: "))

total = branco + nulo + validos

branco2 = (branco / total) * 100
nulo2 = (nulo / total) * 100
validos2 = (validos / total) * 100

print(f"O total de votos foram: {total:.0f}")
print(f"A porcentagem de votos brancos foram: {branco2:.0f}%")
print(f"A porcentagem de votos nulos foram: {nulo2:.0f}%")
print(f"A porcentagem de votos válidos foram: {validos2:.0f}%")