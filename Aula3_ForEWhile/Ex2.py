# Solicita ao usuário um número inteiro positivo
N = int(input("Digite um número inteiro positivo: "))

# Inicializa o fatorial duplo como 1
fatorial_duplo = 1

# Verifica se o número é positivo
if N > 0:
    # Multiplica todos os números pares menores ou iguais a N
    for i in range(2, N + 1, 2):
        fatorial_duplo *= i
    
    print(f"O fatorial duplo de {N} é {fatorial_duplo}.")
else:
    print("Por favor, digite um número inteiro positivo.")