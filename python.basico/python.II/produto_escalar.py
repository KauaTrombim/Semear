#G.A me dá calafrios

vetorString = input("Insira coordenadas de um vetor, separado por espaços (Ex: a b ...): ").split()
vetor =[int(num) for num in vetorString]
escalar = int(input("Insira o escalar: "))

#list para evitar o lazyComputation
novoVetor = list(map(lambda y: y * escalar ,vetor))
print(f"Seu novo vetor é {novoVetor}")