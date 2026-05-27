class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcularMedia(self):
        return (self.nota1 + self.nota2)/2
    def verificarAprovacao(self):
        if(self.calcularMedia() >= 6): print(f"aluno {self.nome} Aprovado")
        else: print(f"aluno {self.nome} Repovado")