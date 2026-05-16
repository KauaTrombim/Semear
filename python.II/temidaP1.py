notasP1 = {
    "Breno" : 10,
    "Gustavo": 10,
    "Benja": 2,
    "Benjinha" : 3,
    "Sorriso" : 8,
    "Lisa" : 2000, #aluna top essa slc
    "Plankton": 4,
    "Juninho ruindade pura" : 2,
    "Cleyton" : 6,
    "Charlie Cox" : 3, #Advogados não sabem integrar
    "Antônio Stark": 10, #Gênio, era a primeira característica mesmo
    "Bruno" : 7,
    "Arthur" : 3,
    "Gabriel" : 9,
    "Guilherme" : 2,
    "Yago" : 1,
    "Elias" : 6,
    "Paulo" : 8,
    "Matias" : 5,
    "João Marcos" : 4 #Separado de Paulo para evitar desavenças
}

nome = input("Digite o nome de um aluno: ").strip()

if not nome in notasP1:
    print("Não conheço esse aluno BIp Bop")
else: print(f"Nota de {nome} foi {notasP1[nome]}")
if nome == "Lisa":
    print("Exemplar, não?")