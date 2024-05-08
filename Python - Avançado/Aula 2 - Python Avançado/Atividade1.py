# Treinando e Usando DEF em Python

def cadastro():
    nomes = ["","","","",""]
    senhas = ["","","","",""]
    cont = 0

    for x in range(3):
        nomes[x] = str(input("Insira o seu nome: "))
        senhas[x] = str(input(f"Insira a senha de nomes: "))

def imprime_nome(x):
    print(f"Nome: {x}")

def piramide_numerica(a):
    for y in range(a):
        for x in range(y+1):
            print(y+1, end=" ")
        print()

def piramide_numerica_inversa(n):
    for y in range(n):
        for x in range(y+1):
            print(x+1, end=" ")
        print()

def contador_vogais_e_espacos(texto):
    cont = 0
    totalvogais = 0

    for i in range(len(texto)):
        if texto[i] == " ":
            cont = cont + 1

        elif texto[i] in "aeiouAEIOU":
            totalvogais = totalvogais + 1
    print(f"O número total de espaços é: {cont}\nO número total de vogais é: {totalvogais}")

def estoque(produto,quantidadetotal,valor):
    total = quantidadetotal*valor
    return total
