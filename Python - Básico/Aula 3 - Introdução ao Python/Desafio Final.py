# Obter entrada do usuário para o primeiro horário
hora1 = int(input("Digite a Hora: "))
minuto1 = int(input("Digite os Minutos: "))

# Obter entrada do usuário para o segundo horário
hora2 = int(input("Digite a Hora 2: "))
minuto2 = int(input("Digite os Minutos: "))

# Somar as horas e os minutos
horatotal = hora1 + hora2
mintotal = minuto1 + minuto2

# Verificar se os minutos ultrapassam 60 e ajustar
if mintotal >= 60:
    mintotal -= 60
    horatotal += 1

# Verificar se a hora total ultrapassa 12 e ajustar
if horatotal > 12:
    horatotal -= 12

# Formatar horas e minutos para garantir dois dígitos
horatotal_formatado = str(horatotal).zfill(2)
mintotal_formatado = str(mintotal).zfill(2)

# Exibir o horário de saída
print(f"A hora de saída é: {horatotal_formatado}:{mintotal_formatado}")

