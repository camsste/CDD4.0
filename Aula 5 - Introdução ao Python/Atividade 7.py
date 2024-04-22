#Faça um código que receba 4 números e realize soma deles e média entre eles e mostre os resultados
soma = 0
for x in range(4):
    num = int(input("Insira um número: "))
    soma = soma + num
media = soma/4
print(f"Sua média é {media}")