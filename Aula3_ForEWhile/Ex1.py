numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Inicializa o fatorial como 1
fatorial = 1

# Calcula o fatorial usando um laço
for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")