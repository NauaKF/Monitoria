# Solicitar o número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Imprimir a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#O input coleta o número digitado pelo usuário.

#O for percorre os números de 1 a 10 (range(1, 11)).

#Para cada valor de i, o código calcula a multiplicação (numero * i) e imprime o resultado de forma formatada.