idade = int(input("Digite a idade (0-150): "))
while idade < 0 or idade > 150:
    print("Idade inválida!")
    idade = int(input("Digite uma idade válida entre 0 e 150: "))
print(f"Idade {idade} registrada com sucesso.")