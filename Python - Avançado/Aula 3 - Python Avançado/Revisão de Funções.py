def Soma(x,y):
    somar = x + y
    print (somar)

def Cadastro():
    nomes=["", "", "", "", "", ""]
    senhas=["", "", "", "", "", ""]
    for x in range(5):
        nomes[x] = input("Digite o nome de usuário: ")
        senhas[x] = input("Digite a senha do usuário: ")

def Somar(*numeros):
    soma =0
    for x in range(len(numeros)):
        soma += numeros[x]
    print(soma)

def Vogais(texto):
    for x in ():
        if x in 'aeiouAEIOU':
            soma+=1
    print(f"Total de vogais é: {soma}")

def Piramide(num):
    for x in range (1,num+1):
        for y in range (1,x+1):
            print (x, end=" ")
        print( )

def Piramide2(num):
    for x in range(1,num+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()

def TratarTexto(texto):
    soma =0
    for x in range (len(texto)):
        if texto[x] != " " and texto[x] != "." and texto[x] != "," and texto[x] != "!":
            soma += 1
    print(soma)
    for y in range(len(texto)-1,-1,-1):
        print(texto[y], end="")

def ListaUnica(l):
    NovaLista = []
    for x in l:
        if x not in NovaLista:
            NovaLista.append(x)
    print(NovaLista)

def Duplicados(*lista):
    nova=set(lista)
    print(f"Lista recebida {lista}")
    print(f"Lista sem repetição {nova}")

def Dupli2(*lista):
    Listanova= []
    for x in lista:
        if x not in Listanova:
            Listanova.append(x)
    print(Listanova)

def TestePrimos(x):
    if x == 1:
        return x,"não é um número primo"
    elif x == 2:
        return x,"é um número primo"
    else:
        for y in range(2,x):
            if (x%y== 0):
                return x,"Número não é primo"
            else:
                return x,"É primo"