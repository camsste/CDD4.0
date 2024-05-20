class ContaBancaria():
    def __init__(self, nome, numero, tipo):
        self.nome = nome
        self.numero = numero
        self.tipo = tipo
        self.status = False
        self.saldo = 0.0

    def contaAtivar(self):
        if self.status == False:
            self.status = True
            print(f"Conta ativada com sucesso!")
        else:
            print(f"Conta encontra-se ativada")

    def contaDesativar(self):
        if self.status == True:
            self.status = False
            print(f"Conta desativada com sucesso!")
        else:
            print(f"Conta encontra-se desativada")

    def depositar(self,valordeposito):
        if self.status == True:
            self.saldo+=valordeposito
            print(f"Deposito realizado com sucesso")
        else:
            print(f"Conta não permite movimentação, conta inativa!")

    def sacar(self,valorsaque):
        if self.status == True:
            if self.saldo >= valorsaque:
                self.saldo -= valorsaque
                print(f"Saque realizado com sucesso!")
            else:
                print(f"Saldo Insuficiente!")
        else:
            print(f"Conta não permite movimentação, conta inativa!")

    def saldoverificar(self):
        if self.status == True:
            print(f" O seu saldo da conta é {self.saldo}")
        else:
            print(f"Conta não permite movimentação, conta inativa!")