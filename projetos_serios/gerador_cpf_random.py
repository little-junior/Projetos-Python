import random

for i in range(10):
    cpf_random = ""

    for i in range(9):
        cpf_random += str(random.randint(0,9))
        
    

    #Definindo o primeiro dígito
    soma_1 = 0
    cont_1 = 10

    for i in cpf_random:
        
        checagem = int(i) * cont_1
        soma_1 = soma_1 + checagem
        cont_1 -= 1

    resultado_primeiro_digito = (soma_1 * 10) % 11

    primeiro_digito = 0 if resultado_primeiro_digito > 9 else resultado_primeiro_digito

    print("O primeiro digito é:", primeiro_digito)

    #Definindo o segundo dígito
    cpf_random += str(primeiro_digito)

    soma_2 = 0
    cont_2 = 11

    for i in cpf_random:
        
        checagem = int(i) * cont_2
        soma_2 = soma_2 + checagem
        cont_2 -= 1

    resultado_segundo_digito = (soma_2 * 10) % 11

    segundo_digito = 0 if resultado_segundo_digito > 9 else resultado_segundo_digito

    print("O segundo digito é:", segundo_digito)

    novo_cpf = cpf_random + str(segundo_digito)


    print(novo_cpf)






