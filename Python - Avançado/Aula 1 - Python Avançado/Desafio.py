opcao = -5
nomes = ["","","","",""]
senha = ["","","","",""]
cont = 0

while opcao != 3:
    opcao = int(input("Opções:\n1- Cadastro:\n2- Login:\n3- Sair:\nSelecione: "))

    if opcao == 1:
        for x in range(5):
            nomes[x] = str(input("Digite seu nome de usuário: "))
            senha[x] = str(input(f"Digite a senha de {nomes[x]}: "))

    elif opcao == 2:
        login = str(input("Insira seu nome de usuário: "))
        senha = str(input("Insira a sua senha: "))
        for y in range(5):
            if login == nomes[y]:
                if senha == senha[y]:
                    print("Login efetuado com sucesso!")
                else:
                    print("Senha incorreta")
            else:
                cont = cont + 1
        if cont == 5:
            print("Esse usuário não existe")