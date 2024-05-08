a = ["", "", "", "", "", "", "", "", "", ""]
m = ["", "", "", "", "", "", "", "", "", ""]
for i in range(10):
    a[i] = float(input(f"Digite um número {i+1}: "))

x = float(input("Digite o multiplicador: "))

for y in range(10):
    # Para multiplicar todos os espaços "m" pelo multiplicador
    m[y] = a[y] * x
    print(m)