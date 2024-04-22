#Faça um algoritmo que leia a idade de uma pessoa expressa em anos,meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerando o ano com 365 dias e mês com 30 dias
idade = int(input("Escreva sua idade: "))
mes = int(input("Escreva o seu mês em número: "))
dias = int(input("Escreva os dias que você têm: "))

anos = idade*365
mes_dias = mes*30

diastotais = anos+mes_dias+dias

print(f"Você possui {diastotais} dias de vida")

