inicio = int(input("Início: "))
fim = int(input("Fim: "))

i = inicio
while i <= fim:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1