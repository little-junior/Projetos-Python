while True:
    try:
        num_1 = float(input("Digite o primeiro número: "))
        num_2 = float(input("Digite o segundo número: "))
        operador = input("Digite qual operação você deseja efetuar ( 1: + / 2: - / 3: * / 4: /): ")

        if operador == "1":
            soma = num_1 + num_2
            print(f'{soma=}')
        elif operador == "2":
            sub = num_1 - num_2
            print(f'{sub=}')
        elif operador == "3":
            mult = num_1 * num_2
            print(f'{mult=}')
        elif operador == "4":
            div = num_1 / num_2
            print(f'{div=}')
        else:
            print("Operador não compreendido.")

        request = input("Deseja sair? 's' para sim e 'n' para nao: ").startswith('s')
        if request:
            break

    except:
        print("Algum erro foi detectado. Tente novamente")





