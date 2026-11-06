orcamento = float(input("Digite o orçamento máximo: "))
total_gasto = 0
continuar = True

while continuar:
    gasto = float(input(f"Gasto atual (Total: {total_gasto}). Digite o valor ou negativo para sair: "))
    
    if gasto < 0:
        break
    
    if total_gasto + gasto > orcamento:
        print("Orçamento excedido! Não é possível adicionar este gasto.")
        break
    else:
        total_gasto += gasto
        
    if total_gasto >= orcamento:
        break

print(f"\nResumo Final:")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Sobrou: R$ {orcamento - total_gasto:.2f}")