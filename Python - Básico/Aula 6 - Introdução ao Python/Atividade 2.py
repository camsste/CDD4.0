# Faça um código que receba o valor da base e da altura de um triângulo e calcule sua área. Usando a fórmula A= (base x altura) /2
triangulo = 1
quadrado = 2
resposta = 0
while resposta !=3:
    resposta = int(input("Qual a sua opção:\n"
                          "1 = àrea do triângulo\n"
                          "2 = área do quadrado\n"
                          "3 = parar\n "))
    if resposta == 1:
        print(f"Para descobrir a àrea do triângulo, preencha as informações a seguir.")
        base = float(input("Base do triângulo em cm: "))
        altura = float(input("Altura do triângulo em cm: "))
        area1 = (base*altura)/2
        print(f"A sua área é {area1}cm")

    elif resposta == 2:
        print(f"Para descobrir a àrea do quadrado, preencha as informações a seguir.")
        base = int(input("Lado do quadrado em cm: "))
        area2 = base * base
        print(f"A sua área é {area2}cm")

    elif resposta > 3 or resposta < 0:
        print(f"O número que você digitou é inválido!")