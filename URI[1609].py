qtd = int(input())

for r in range(qtd):
    qtd_ram = int(input())
    rams = [int(x) for x in input().split()]
    print(len(set(rams)))
