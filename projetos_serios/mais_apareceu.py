frase = input("Digite sua frase: ").replace(" ", "")

i = 0
quant_letra_mais = 0
letra_mais = ""

for i in frase:
    
    letra_atual = i
    contagem_letra_atual = frase.count(letra_atual)


    if contagem_letra_atual > quant_letra_mais:
        quant_letra_mais = contagem_letra_atual 
        letra_mais = letra_atual
    


print(f'A letra que mais aparece é {letra_mais} com um total de {quant_letra_mais} aparições')