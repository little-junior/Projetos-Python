import os


# # #Entrada do CPF pelo usuário
while True:
      
    cpf_usuario = input("Digite seu cpf com pontuação: ")

    if len(cpf_usuario) == 14:
        cpf_completo = cpf_usuario.replace(".", "").replace("-","")
        cpf_formatado = cpf_completo[:9]
    else:
        os.system('cls')
        print("Digite corretamente o cpf.")
        continue

    #Definindo o primeiro dígito
    soma_1 = 0
    cont_1 = 10

    for i in cpf_formatado:
        
        checagem = int(i) * cont_1
        soma_1 = soma_1 + checagem
        cont_1 -= 1

    resultado_primeiro_digito = (soma_1 * 10) % 11

    primeiro_digito = 0 if resultado_primeiro_digito > 9 else resultado_primeiro_digito

    print("O primeiro digito é:", primeiro_digito)

    #Definindo o segundo dígito
    cpf_formatado += str(primeiro_digito)

    soma_2 = 0
    cont_2 = 11

    for i in cpf_formatado:
        
        checagem = int(i) * cont_2
        soma_2 = soma_2 + checagem
        cont_2 -= 1

    resultado_segundo_digito = (soma_2 * 10) % 11

    segundo_digito = 0 if resultado_segundo_digito > 9 else resultado_segundo_digito

    print("O segundo digito é:", segundo_digito)

    novo_cpf = cpf_formatado + str(segundo_digito)


    #Validação final
    if novo_cpf == cpf_completo:
        print(f'{cpf_usuario} é válido.')
    else:
        print(f'{cpf_usuario} não é válido.')
    
    #Input de saida (break ou continue) 
    saida = input("Quer sair? [s]im [n]ão ").lower()
    if saida == "s":
        break


##testando commit