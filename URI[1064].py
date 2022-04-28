valores = []
for i in range(6):
    valores.append(float(input()))

valoresPositivos = 0
somaPositivos = 0
for v in valores:
    if v > 0:
        somaPositivos += v
        valoresPositivos += 1
print(valoresPositivos, "valores positivos")
print('%.1f' % (somaPositivos/valoresPositivos))