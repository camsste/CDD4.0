mes = int(input("Qual foi o mês que você nasceu?"))
dia = int(input("Qual foi o dia que você nasceu?"))
ano = int(input("Qual foi o ano que você nasceu?"))

mestotal = mes * 30
anototal = (2024 - ano) * 365
total = mestotal + anototal + dia
meses = total / 12
idade = ano / 2024

print(f"Os dias totais de vida são: {total}")
print(f"Os meses totais de vida são: {meses}")
print(f"A sua idade é: {idade}")