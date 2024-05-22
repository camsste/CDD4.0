class Ingresso():
    def __init__(self, valor):
        self.valor=valor
    def imprimeIngresso(self):
        print(f"O valor do ingresso é {self.valor}")
class IngressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def imprimeIngresso(self):
        vip = self.valor * 1.5
        print(f"O valor do ingresso vip é: {vip}")
