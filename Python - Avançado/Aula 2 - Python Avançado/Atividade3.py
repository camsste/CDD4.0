#Importando de outro arquivo da mesma pasta uma função
from Atividade1 import *
produto = input("Digite o nome do produto: ")
quantidadetotal = int(input("Digite a quantidade do produto: "))
valor = float(input("Digite o preço do produto: "))

retorno = estoque(produto,quantidadetotal,valor)
print(retorno)