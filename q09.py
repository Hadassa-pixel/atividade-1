opcao = 0
while opcao != 3:
    print("\n--- MENU ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Sair")
    opcao = int(input("Escolha: "))
    
    if opcao == 1:
        n1 = float(input("N1: "))
        n2 = float(input("N2: "))
        print(f"Resultado: {n1 + n2}")
    elif opcao == 2:
        n1 = float(input("N1: "))
        n2 = float(input("N2: "))
        print(f"Resultado: {n1 - n2}")