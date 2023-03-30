print(10 * "-" ,"GUESS THE NUMBER", 10 * "-")

print("Estou pensando em um número de 0 a 10. Tente adivinhá-lo!")

while True:

    import random

    numero_certo = random.randint(0, 10)

    print("Qual número você acha que estou pensando?")

    while True:
        numero_adivinhado = int(input())

        if numero_adivinhado < numero_certo:
            print("O número que você digitou está abaixo do que estou pensando. Continue tentando!")
        elif numero_adivinhado > numero_certo:
            print("O número que você digitou está acima do que estou pensando. Continue tentando!")
        else:
            print("Parabéns! Você acertou.")
            break
        
    saida = input("Fim do jogo! Você deseja continuar ou sair? [s] ou [c]: ")
    
    if saida == 's':
        break
    elif saida == 'c':
        continue
    else:
        break


