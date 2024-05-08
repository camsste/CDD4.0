notas = ["","","","",""] #Vetor Array
soma = 0
cont = 0
for x in range(5):
    # Para saber a nota dos alunos da lista (array)
    notas[x] = float(input("Digite a nota dos alunos: "))

for z in range(5):
    # Sistema de Repetição para calcular a nota
    soma = soma + notas[z]
media = soma / 5

for i in range(5):
    # Sistema de condição para decidir aprovação ou reprovação
    if notas[i] >= media:
    # Sistema para contar a quantidade de alunos usando um sistema de acumulação
        cont +=1

print(f"A média da sala foi {media} e {cont} alunos foram aprovados.")

# Pontos:
# Nunca coloque e variável do for igual! Sempre mude!
