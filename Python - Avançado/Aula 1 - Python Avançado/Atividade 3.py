nomes = [0,0,0,0,0]
sennhas = [0,0,0,0,0]
for x in range(5):
    nomes[x] = str(input(f"Digite o nome do usuário: {x+1}"))
    senha[x] = str(input(f"Digite a senha desse usuário: {x+1}"))

for y in range(5):
    print(f"O nome do usuário é {nomes[y]} e a senha é {senha[y]} na posição em {y}")
