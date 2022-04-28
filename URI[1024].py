n = int(input())
for i in range(n):
    msg = str(input())
    passada1 = ''
    for x in msg:
        if x.isalpha():
            passada1 += chr(ord(x) + 3)
        else:
            passada1 += x

    passada2 = passada1[::-1]

    metade = int(len(passada2)/2)
    metade1 = passada2[0:metade]
    metade2 = passada2[metade:]

    passada3 = ''

    for c in metade2:
        passada3 += chr(ord(c)-1)

    print(metade1+passada3)
