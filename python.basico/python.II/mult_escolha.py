
#Um objeto básico que possibilita expansão
pergunta = {
    "Comando": "Qual personagem da Marvel nunca teve posse de duas joias do infinito?",
    "a": "Loki",
    "b": "Ronan",
    "c": "Capitão América",
    "d": "Homem Aranha",
    "Correta" : "b"
}  

def printPergunta(p):
    print(p["Comando"])
    print(f"a) {p['a']}")
    print(f"b) {p['b']}")
    print(f"c) {p['c']}")
    print(f"d) {p['d']}")


#Inicio
printPergunta(pergunta)
alternativa = input("Digite uma alternativa: ")[0]

if alternativa == pergunta["Correta"]: print("Acertou! ;)")
else: print("Péeeh, errado :/")

