class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.area = self.definirArea()
        self.perimetro = self.definirPerimetro()
    def definirArea(self):
        return self.largura * self.altura
    def definirPerimetro(self):
        return (2 *self.largura) + (2 * self.altura)
    def getArea(self):
        return self.area
    def getPerimetro(self):
        return self.perimetro