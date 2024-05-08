#Cinco números em array
numero = ["","","","",""]
for x in range(5):
    numero [x] = float(input(f"Digite um número {x+1} "))

for y in range(4, -1, -1):
    print(numero[y], end = " ")