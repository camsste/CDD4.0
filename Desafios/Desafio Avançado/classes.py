class Pessoa():
    def __init__(self,nome,peso,idade,comendo,falando,dormindo):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self, comida):
        if self.falando == True:
            print(f"{self.nome} está falando.")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo.")
        elif self.comendo == True:
            print(f"{self.nome} já está comendo.")
        else:
            print(f"{self.nome} foi comer {comida}.")
            self.comendo = True

    def falar(self, frase):
        if self.comendo == True:
            print(f"{self.nome} está comendo.")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo.")
        elif self.falando == True:
            print(f"{self.nome} já está falando.")
        else:
            print(f"{self.nome} disse '{frase}'")
            self.falando = True

    def dormir(self, horario):
        if self.comendo == True:
            print(f"{self.nome} está comendo.")
        elif self.falando == True:
            print(f"{self.nome} está falando.")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo.")
        else:
            print(f"{self.nome} dormiu às {horario}.")
            self.dormindo = True

    def pararDormir(self):
        if self.dormindo == False:
            print(f"{self.nome} não está dormindo.")
        else:
            print(f"{self.nome} acordou.")
            self.dormindo = False

    def pararFalar(self):
        if self.falando == False:
            print(f"{self.nome} não está falando.")
        else:
            print(f"{self.nome} se calou.")
            self.falando = False

    def pararComer(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo.")
        else:
            print(f"{self.nome} fechou a boca.")
            self.comendo = False



