# Inicializar variáveis
soma = 0
contador = 0

# Enquanto o usuário não digitar zero
while True:
    # Solicitar ao usuário que digite um número
    numero = float(input("Digite um número (digite 0 para parar): "))
    
    # Verificar se o número é zero para parar
    if numero == 0:
        break
    
    # Somar o número e incrementar o contador
    soma += numero
    contador += 1

# Verificar se pelo menos um número foi digitado para evitar divisão por zero
if contador > 0:
    # Calcular e exibir a média
    media = soma / contador
    print(f"A média dos números digitados é: {media:.2f}")
else:
    print("Nenhum número válido foi digitado.")

#O algoritmo usa duas variáveis: soma para acumular a soma dos números e contador para contar quantos números válidos foram digitados.

#O laço while True mantém o programa pedindo números até o usuário digitar zero.

#Se o número digitado for zero, o laço é interrompido com break.

#A soma e o contador são atualizados apenas se o número não for zero.

#Após a interrupção, a média é calculada dividindo a soma pela quantidade de números digitados. 
#A média é exibida com duas casas decimais. Se nenhum número válido foi digitado, 
#o programa avisa que não foi possível calcular a média.