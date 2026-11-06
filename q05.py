soma = 0
num = int(input("Digite um número (0 para sair): "))
while num != 0:
    soma += num
    num = int(input("Digite o próximo número (0 para sair): "))
print(f"A soma total é: {soma}")