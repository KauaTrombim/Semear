import math
import sys

#Abordagem bruta, deixa o programa todo O(n²)
def isPrimo(num):
    min = 2
    if num < min: return False
    max = int(math.sqrt(num))
    for i in range (min, max+1):
        if num % i == 0: return False
    return True

#Main
teto = int(input("Digite um teto "))

if teto < 2: 
    print("Número invalido, colega")
    sys.exit()

#Percorre todos os primos
tmp = teto
totalPrimos = 1
while (tmp > 2):
    if isPrimo(tmp): totalPrimos += 1
    tmp -= 1

print(f"O total de primos entre 2 e {teto} é {totalPrimos}")