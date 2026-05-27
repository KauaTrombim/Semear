def duplicar (num):
    return num * 2

lista = [1, 7, 14, 15, 19, 24, 32, 56]
soma = map(duplicar, lista)
print(f"A soma da lis(t)a é {soma}")