import requests

print("Verificando endereço")
cep = input("Digite o seu CEP: ")
if len(cep) !=8:
    print("CEP INVÁLIDO!")
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
print(consulta.json())