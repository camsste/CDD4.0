# Faça um código que recebe o número de alunos de uma sala de aula e depois solicitar as notas desses alunos, no final, mostre a média aritmética da turma usando "while"

soma = 0
c = 0
alunos = float(input("Digite o número de alunos da sua sala: "))

while alunos > c:
    a = float(input("Digite as notas: "))
    soma = soma + a
    c = c + 1

media = soma/alunos
print(f"A média da sua sala é: {media}")
