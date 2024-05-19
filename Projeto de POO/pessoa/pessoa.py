class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.acao_atual = None  # Nenhuma ação sendo realizada inicialmente

    def comer(self):
        if self.acao_atual is not None:
            print(f"{self.nome} não pode comer porque está {self.acao_atual}.")
        else:
            self.acao_atual = 'comendo'
            print(f"{self.nome} está agora comendo.")
    
    def falar(self):
        if self.acao_atual is not None:
            print(f"{self.nome} não pode falar porque está {self.acao_atual}.")
        else:
            self.acao_atual = 'falando'
            print(f"{self.nome} está agora falando.")
    
    def dormir(self):
        if self.acao_atual is not None:
            print(f"{self.nome} não pode dormir porque está {self.acao_atual}.")
        else:
            self.acao_atual = 'dormindo'
            print(f"{self.nome} está agora dormindo.")
    
    def parar(self):
        if self.acao_atual is not None:
            print(f"{self.nome} parou de {self.acao_atual}.")
            self.acao_atual = None
        else:
            print(f"{self.nome} não está realizando nenhuma ação no momento.")
