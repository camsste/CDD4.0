litros = float(input("Quantos litros foi abastecido: "))
combustivel = input("Qual foi o tipo de Combustível (E para E-tanol, G para Gasolina): ")

E = 4.90 * litros
G = 5.80 * litros

if combustivel.lower() == 'e':
    print(f"Você gastou R$ {E} em E-tanol")
elif combustivel.lower() == 'g':
    print(f"Você gastou R$ {G} em Gasolina")
else:
    print("Tipo de combustível inválido.")
