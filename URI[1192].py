numeroEntradas = int(input())
entradas = []


def pegarEntradas():
    for n in range(numeroEntradas):
        entradas.append(input())
    return None


def definirOperacao():
    for n in entradas:
        primeiroNum, letra, segundoNum = list(n)
        primeiroNum = int(primeiroNum)
        segundoNum = int(segundoNum)
        if primeiroNum == segundoNum:
            print(primeiroNum*segundoNum)
        elif letra.isupper():
            print(segundoNum - primeiroNum)
        else:
            print(segundoNum + primeiroNum)
    return None


pegarEntradas()
definirOperacao()
