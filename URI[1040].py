def calcularMedia(listaNotas):
    n1, n2, n3, n4 = listaNotas
    media = (n1*2 + n2*3 + n3*4 + n4 * 1)/10
    return media


def calcularExame(notaAnterior, novaNota):
    mediaExame = (notaAnterior + novaNota)/2
    return mediaExame


notas = list(map(float, input().split()))
resultado = calcularMedia(notas)

print("Media: %.1f" % resultado)
if resultado >= 7.0:
    print("Aluno aprovado.")
elif resultado < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: %.1f" % notaExame)
    resultadoExame = calcularExame(resultado, notaExame)
    if resultadoExame >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % resultadoExame)
