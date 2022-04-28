D, N = input().split()

while D != "0" and N != "0":
    saida = N.replace(D, '')
    if saida == '':
        saida = 0
    print(int(saida))
    D, N = input().split()
