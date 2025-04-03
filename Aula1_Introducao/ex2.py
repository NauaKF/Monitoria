# Solicitar os valores da base e altura ao usuário
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

# Calcular a área do triângulo
area = (base * altura) / 2

# Exibir a mensagem com a área calculada
print(f"A área do triângulo com base {base} e altura {altura} é: {area:.2f}")

#O algoritmo solicita ao usuário os valores da base e da altura do triângulo com input(), 
#convertendo-os para float para permitir números decimais.

#A área do triângulo é calculada utilizando a fórmula: área = base*altura/2.

#O resultado é exibido na tela com a mensagem solicitada, utilizando f-strings para formatar a saída.