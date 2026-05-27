CONSTANTE_DE_CONVERSAO = 3.28084

def metro_to_feet(metro):
    return metro * CONSTANTE_DE_CONVERSAO

metro = float(input("Digite o valor em metros: "))
feet  = metro_to_feet(metro)

print(f"O valor convertido é de {feet} pés.")