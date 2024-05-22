class Atleta():
    def __init__(self, aposentado, peso):
        pass

    def aposentado(self):
        pass

    def aquecer(self):
        pass

class Corredor(Atleta):
    def __init__(self, correr, descansar, aquecer ):
        super().__init__()
        self.correr = correr
        self.descansar = descansar
        self.aquecer = aquecer

    def correr(self):
