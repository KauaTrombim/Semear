KELVIN_CONSTANT = 273.15

def celsius_to_fahrenheit(celsius):
    return 1.8 * celsius + 32
def celsius_to_kelvin(celsius):
    return celsius + KELVIN_CONSTANT

#Inicio do programa
valor = float(input("Digite a temperatura em Celsius: "))
print(f"A temperatura em Fahrenheit é de: {celsius_to_fahrenheit(valor)} °F")
print(f"A temperatura em Kelvin é de: {celsius_to_kelvin(valor):.2f} °K")