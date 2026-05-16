import sys

vetor1String = input("Insira coordenadas de um vetor, separado por espaços (Ex: a b ...): ").split()
vetor1 =[int(num) for num in vetor1String]

vetor2String = input("Insira coordenadas de um segundo vetor: ").split()
vetor2 =[int(num) for num in vetor2String]

if len(vetor1) != len(vetor2):
    print("Os vetores tem tamanhos diferentes >:(")
    sys.exit()

op = input("Digite a operação: ")
rst = []
match(op):
    case "+":
        for i in range(len(vetor1)):
            rst.append(vetor1[i]+vetor2[i])
    case "*":
        for i in range(len(vetor1)):
            rst.append(vetor1[i]*vetor2[i])
    case _:
        print("Comando invalido :(")
        sys.exit()
print(rst)