# Inicializar a soma como 0
soma = 0

# Enquanto o usuário não digitar um número negativo
while True:
    # Solicitar um número inteiro positivo
    numero = int(input("Digite um número inteiro positivo (ou um número negativo para parar): "))
    
    # Verificar se o número é negativo
    if numero < 0:
        break  # Interromper o laço se o número for negativo
    
    # Somar o número positivo à soma total
    soma += numero

# Exibir o resultado final da soma
print(f"A soma dos números digitados é: {soma}")

#A variável soma é inicializada com 0 para armazenar a soma dos números positivos.

#O laço while True garante que o programa continue pedindo números até que o usuário decida parar, 
#digitando um número negativo.

#O input solicita um número do usuário e o converte para inteiro com int().

#Se o número digitado for negativo (if numero < 0), o laço é interrompido com break.

#Caso o número seja positivo, ele é somado à variável soma.

#Após o laço ser interrompido, a soma dos números digitados é exibida.