class Animal:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        print("Este animal faz algum som")

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome}: Auau")

class Gato(Animal):
    def falar(self):
        print(f"{self.nome}: Miau")