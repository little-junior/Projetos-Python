import os

lista = []

while True:    
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar [t]erminar: ").lower()

    if opcao == "i":
        os.system('cls')
        inserir = input("Digite qual item você quer inserir na lista: ")
        lista.append(inserir)
    
    elif opcao == "a":
        try:
            apagar = input("Digite o índice do item da lista que você deseja apagar: ")
            del lista[int(apagar)]
            os.system('cls')
            print("Item excluido.")
        except:
            os.system('cls')
            print("Não é possível apagar esse item.")
    
    elif opcao == "l":
        os.system('cls')
        if lista == []:
            print("Nada a listar.")
        for indice, item in enumerate(lista):
            print(indice, item)

    elif opcao == "t":
        os.system('cls')
        print("Você finalizou sua lista. Boas Compras!")
        print("Segue seus itens para compra:")
        print(20 * "-")
        for i in lista:
            print (i)
        break
    
    else:
        os.system('cls')
        print("Opção não disponível.")
        

    


