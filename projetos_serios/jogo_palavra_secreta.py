palavra_secreta = "banana"
palavra_formatada = len(palavra_secreta) * ["*"] 


while True:
    
    for i in range(1, 100):
        letra = input("Digite uma letra: ")
        
        if len(letra) > 1:
            print("Digite apenas uma letra.")
            continue

        if letra in palavra_secreta:
            for j in range(len(palavra_secreta)):
                if letra == palavra_secreta[j]:
                    palavra_formatada[j] = letra
            
        
        print("Palavra formatada:", "".join(palavra_formatada))
    
        if "".join(palavra_formatada) == palavra_secreta:
            print("Parabéns! Você acertou!")
            print(f"Total de tentativas: {i}")
            break
    break


