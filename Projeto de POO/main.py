import sys
print(sys.path)

from pessoa.pessoa import Pessoa

def main():
    pessoa1 = Pessoa("João", 30, 1.75)

    pessoa1.comer()    # João está agora comendo.
    pessoa1.falar()    # João não pode falar porque está comendo.
    pessoa1.parar()    # João parou de comendo.
    pessoa1.falar()    # João está agora falando.
    pessoa1.dormir()   # João não pode dormir porque está falando.
    pessoa1.parar()    # João parou de falando.
    pessoa1.dormir()   # João está agora dormindo.

if __name__ == "__main__":
    main()
