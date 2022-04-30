D, N = input().split()

while D != "0" and N != "0":
    output = N.replace(D, '')
    if output == '':
        output = 0
    print(int(output))
    D, N = input().split()
