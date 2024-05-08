# Crie um algoritmo que receba 3 números e informe o maior entre eles
A = int(input("Escreva o primeiro número: "))
B = int(input("Escreva o segundo número: "))
C = int(input("Escreva o terceiro número: "))

if A > B and A > C:
    print(f"O número maior entre os três é {A}")
elif B > A and B > C:
    print(f"O número maior entre os três é {B}")
else:
    print(f"O número maior entre os três é {C}")