# Solicitar o número N ao usuário
N = int(input("Digite um número para ver os primeiros N termos da sequência Fibonacci: "))

# Inicializar os dois primeiros termos da sequência Fibonacci
a, b = 0, 1

# Imprimir os primeiros N termos
print("Sequência Fibonacci:")
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b  # Atualizar os valores de a e b

#O código solicita que o usuário digite um número N, que indica quantos termos da sequência Fibonacci 
# ele deseja ver.

#Inicializa os dois primeiros termos da sequência como 0 e 1 (a = 0 e b = 1).

#O laço for itera N vezes, imprimindo o valor atual de a (o termo atual da sequência) e, em seguida, 
#atualiza os valores de a e b para os próximos termos da sequência usando a fórmula 𝑎=𝑏 e b=a+b.

#A função end=" " é usada para garantir que os números sejam impressos na mesma linha, separados por espaço.