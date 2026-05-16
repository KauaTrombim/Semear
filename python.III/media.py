def calcularMedia(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3

notasString = input("Digite as 3 notas separadas por vírgula: ").split()
notas = [int(n) for n in notasString]

media = calcularMedia(notas[0], notas[1], notas[3])
print(f"A media é {media}")