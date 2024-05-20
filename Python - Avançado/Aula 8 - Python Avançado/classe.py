class Forma():
    def __init__(self):
        pass

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print(f"A área desse Retângulo é {area}")

    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print(f"O perímetro desse Retângulo é {perimetro}")

class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2):
        super().__init__()
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        print(f"A área do Triângulo é {area}")

    def calcular_perimetro(self):
        perimetro = self.base + self.lado1 + self.lado2
        print(f"O perímetro desse Triângulo é {perimetro}")