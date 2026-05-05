import math
import sys

def calcular_delta (coeficientes):
    #Essas variáveis não são estritamente necessárias, mas facilitam a leitura
    a = coeficientes[0]
    b = coeficientes[1]
    c = coeficientes[2]
    return (b**2) - (4 * a * c)

def calcular_raizes(coeficiente):
    delta = calcular_delta(coeficientes)
    if delta < 0: return [] #retorna uma lista vazia

    raizes = []
    a = coeficientes[0]
    b = coeficientes[1]
    c = coeficientes[2]

    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    raizes.append(x1)
    if delta == 0: return raizes #retorna a única solução
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)
    raizes.append(x2)
    return raizes #retorna as duas soluções

# Inicio do programa
coeficientesString = input("Digite os coeficientes A, B e C separado por espaços (Ex: Ax^2 + Bx + C): ").split()
coeficientes = [int(x) for x in coeficientesString]
if coeficientes[0] == 0: 
    print("Não é uma equação do segundo grau :/")
    sys.exit(0)

solucoes = calcular_raizes(coeficientes)
if len(solucoes) == 0: print("Não existe solução real")
else:
    print("Solução: ")
    for x in solucoes: print(f"x = {x}")


