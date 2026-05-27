import sys

#Main
ladosText = input("Digite 3 lados de um triangulo separados por virgula (Ex: a b c)").split()
lados = [int(x) for x in ladosText]

#Verifica a validade do triangulo
if lados[0] + lados[1] <= lados[2] or lados[1] + lados[2] <= lados[0] or lados[0] + lados[2] <= lados[1]:
    print("Não forma um triangulo >:(")
    sys.exit()

#Classifica o triangulo
if(lados[0] == lados[1] == lados[2]):
    print("Triangulo Equilatero Detectado")
elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
    print("Triangulo Isóceles Detectado")
else: print("Triangulo Escaleno Detectado (paia)")
