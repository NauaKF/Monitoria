# Solicita ao usuário uma letra
letra = input("Digite uma letra maiúscula: ")

# Contagem regressiva das letras de 'letra' até 'A'
for i in range(ord(letra), ord('A') - 1, -1):
    print(chr(i))