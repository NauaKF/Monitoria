# Definir a senha correta
senha_correta = "1234"

# Solicitar a senha ao usuário até que seja correta
while True:
    senha = input("Digite a senha: ")
    
    # Verificar se a senha está correta
    if senha == senha_correta:
        print("Senha correta! Acesso permitido.")
        break  # Interromper o laço se a senha estiver correta
    else:
        print("Senha incorreta. Tente novamente.")

#A variável senha_correta é definida como "1234".

#O laço while True vai continuar pedindo a senha até que a senha correta seja digitada.

#O input solicita ao usuário que digite a senha.

#Se a senha digitada for igual à senha definida (senha == senha_correta),
#o programa exibe "Senha correta! Acesso permitido." e sai do laço com o break.

#Se a senha estiver incorreta, o programa avisa e solicita a senha novamente.