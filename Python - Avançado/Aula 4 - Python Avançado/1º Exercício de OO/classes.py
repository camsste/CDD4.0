class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo= False, falando= False, dormindo =False):
    #O que está dentro dos parênteses são PARÂMETROS)
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo
     #Atributos do lado esquerdo e lado direito são PARÂMETROS)

    def parardecomer(self):
        print(f"{self.nome} não comeu nada!")
        self.comendo = False
    def comer(self, alimento):
        print(f"{self.nome} falou a frase '{alimento}'")
        self.comendo = True
        if def comer > 1 (nao pode Receber mais de uma resposta)
        print(f"{self.nome} Não pode comer duas comidas ao mesmo tempo porque está comendo {alimento}")

    def parardefalar(self):
        print(f"{self.nome} não falou nada!")
        self.falando = False
    def falar(self, frase):
        print(f"{self.nome} falou a frase '{frase}'")
        self.falando = True

    def parardedormir(self):
        print(f"{self.nome} não está dormindo!")
        self.dormindo = False

    def dormir(self, horas):
        print(f"{self.nome} dormiu {horas} horas.")
        self.dormindo = True
