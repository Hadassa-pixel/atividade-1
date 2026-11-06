horas = int(input("Quantas horas deseja registrar? "))
total_producao = 0
i = 1

while i <= horas:
    peças = int(input(f"Peças produzidas na hora {i}: "))
    total_producao += peças
    i += 1

media = total_producao / horas if horas > 0 else 0
print(f"\nProdução Total: {total_producao}")
print(f"Produção Média por Hora: {media:.2f}")