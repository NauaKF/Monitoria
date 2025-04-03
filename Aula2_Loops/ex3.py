# Solicitar o número N ao usuário
N = int(input("Digite um número N: "))

# Inicializar a variável para armazenar a soma
soma_pares = 0

# Iterar de 1 até N
for i in range(1, N + 1):
    if i % 2 == 0:  # Verificar se o número é par
        soma_pares += i  # Adicionar o número par à soma

# Exibir o resultado
print(f"A soma dos números pares de 1 até {N} é {soma_pares}.")

#O código solicita um número N ao usuário.

#A variável soma_pares é inicializada com 0 para armazenar a soma dos números pares.

#O laço for percorre os números de 1 até 𝑁 (range(1, N + 1)).

#O if i % 2 == 0 verifica se o número é par. Se for, ele é adicionado à variável soma_pares.

#Ao final, o programa exibe a soma dos números pares.