# Solicitar os 3 valores ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Inicializar uma variável para armazenar a soma
soma = valor1 + valor2 + valor3

# Calcular a média utilizando apenas a variável soma
if soma > 0:
    media = soma / 3
    print(f"A média dos três valores é: {media:.2f}")
else:
    print("A soma dos valores não pode ser zero.")

#O algoritmo solicita três valores do usuário: valor1, valor2 e valor3.

#A soma desses valores é armazenada na variável soma.

#O cálculo da média é realizado verificando se a soma é maior que 0 (como parte do if e else para o caso de não querer uma média inválida). Se for, a média é calculada dividindo a soma por 3. Caso contrário, é exibida uma mensagem indicando que a soma não pode ser zero.

#Finalmente, a média é impressa com duas casas decimais.