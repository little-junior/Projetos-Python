import os

while True:
    perguntas = [
        {
            'Pergunta' : "Qual a capital do Brasil?",
            'Questoes' : ["Nova York", "Uruguaiana", "Cidade do México", "Brasilia"],
            'Resposta' : "Brasilia"
        },
        {
            'Pergunta' : "Quantos dias tem numa semana?",
            'Questoes' : [2, 3, 9, 7],
            'Resposta' : 7
        },
        {
            'Pergunta' : "Qual o nome do Presidente do Brasil?",
            'Questoes' : ["Biden", "Che Guevara", "Pedro", "Lula"],
            'Resposta' : "Lula"
        }
    ]

    quantidade_acertos = 0
    for sequencia in perguntas:
        print("Pergunta:", sequencia.get("Pergunta"))
        print()
        pegar_questoes = sequencia['Questoes']
        
        for indice, questao in enumerate(pegar_questoes):
            print(f'{indice}) {questao}')
        
        resposta_user = input("Digite o número da sua resposta: ")
        
        while True:
            try:
                resposta_formatada = int(resposta_user)
                if pegar_questoes[resposta_formatada] == sequencia.get("Resposta"):
                    print("Acertou! 😁")
                    quantidade_acertos +=1
                else:
                    print("Errou! 😢")
                print()
                break
            except ValueError:
                resposta_user = input("Erro. Digite o número da sua resposta corretamente: ")
            except IndexError:
                resposta_user = input("Erro. Digite o número da sua resposta corretamente: ")

    os.system('cls')

    print(f"Você acertou {quantidade_acertos} pergunta(s)")
    
    jogar_novamente = input("Quer jogar novamente? 0 ou 1 | ")
    if jogar_novamente == "0":
        break
    
    os.system('cls')    
