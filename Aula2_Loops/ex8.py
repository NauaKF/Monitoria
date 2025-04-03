# Inicializar a variável soma
soma = 0

# Enquanto a soma não for maior que 100
while soma <= 100:
    # Solicitar ao usuário que digite um número
    numero = float(input("Digite um número: "))
    
    # Somar o número à soma total
    soma += numero

# Exibir a soma final
print(f"A soma dos números digitados é: {soma}")

#A variável soma é inicializada com 0 para armazenar a soma dos números digitados.

#O laço while continua pedindo números enquanto a soma não for maior que 100.

#A cada iteração, o programa solicita um número ao usuário e o adiciona à variável soma.

#Quando a soma ultrapassar 100, o laço é interrompido automaticamente e o programa exibe a 
#soma total dos números digitados.