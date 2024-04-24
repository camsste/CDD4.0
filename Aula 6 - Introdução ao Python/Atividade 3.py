print(f"Vamos descobrir quanto tempo durou o jogo! Vamos lá?")
inicio = int(input("Digite aqui a hora que iniciou o jogo de xadrês:"))
fim = int(input("Digite aqui a hora que terminou:"))

if inicio <= fim:
    duracao = fim - inicio
else:
    duracao = 24 - inicio + fim
print(f"O jogo durou {duracao} horas.")
