# Solicitar o número ao usuário
n = int(input("Digite um número para calcular o fatorial: "))

# Inicializar a variável para armazenar o fatorial
fatorial = 1

# Calcular o fatorial utilizando um laço for
for i in range(1, n + 1):
    fatorial *= i  # Multiplica o fatorial pelo número atual

# Exibir o resultado
print(f"O fatorial de {n} é {fatorial}.")

#O código solicita que o usuário insira um número 𝑛

#A variável fatorial é inicializada com 1, pois o fatorial de qualquer número começa com 1.

# laço for percorre os números de 1 até n (range(1, n + 1)), multiplicando o valor de fatorial 
# pelo número em cada iteração.

#Ao final, o programa exibe o valor do fatorial calculado.