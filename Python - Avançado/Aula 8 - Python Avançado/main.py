from classe import *

if __name__ == "__main__":
    # Criando uma instância de Retângulo e chamando os métodos
    retangulo = Retangulo(5, 3)
    retangulo.calcular_area()
    retangulo.calcular_perimetro()

    # Criando uma instância de Triângulo e chamando os métodos
    triangulo = Triangulo(4, 3, 5, 5)
    triangulo.calcular_area()
    triangulo.calcular_perimetro()