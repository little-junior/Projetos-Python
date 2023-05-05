""" 
primeira parte: dois numeros naturais m e n
segunda parte: formada por m numeros nats
terceira parte: formada por n numeros nats

Etapas de determinação:
- Somar todos os m's nums = sm
- Somar todos os digitos da soma = sd
- Se sd for par, aplicar Método A. Se não, Método B.

* Método A:
- ORDENAR OS NUMEROS DE N CRESCENTEMENTE
- MULTIPLICAR CADA ITEM POR SUA POSIÇÃO (PRIMEIRO ITEM = 1)
- SOMAR TODOS OS NUMEROS, OBTENDO SN

*Método B:
- SOMAR CADA NÚMERO DE N A SEQUENCIA (1, 2, 4, 7, 11, 16...)
- ACUMULAR OS DOIS NÚMEROS A DIREITA
- ACUMULO GERAL = SN

*Descobrindo a data:
- RESTO DA DIVISÃO DE SN POR 31 = dia_final DA INVASAO (0 DE RESTO = dia_final 31)
- DIVISAO INTEIRA DE SN POR 12 = mes_final DA INVASAO (0 = DEZEMBRO)
"""
def descobrir_método (vet_m):
    sm = 0
    for i in vet_m:
        sm = sm + i

    sd = 0
    div_inteira = sm
    while div_inteira != 0:
        digito = div_inteira % 10
        div_inteira = div_inteira // 10
        sd = sd + digito
    
    if sd % 2 == 0:
        return "Método A"
    else:
        return "Método B"

def metodo_a (vet_n, num_vetor):
    for i in range(num_vetor - 1):
        for j in range(i + 1, num_vetor):
            if vet_n[i] > vet_n[j]:
                vet_n[i], vet_n[j] = vet_n[j], vet_n[i] 
    
    for p in range(num_vetor):
        vet_n[p] = vet_n[p] * (p + 1)

    sn = 0
    for q in vet_n:
        sn = sn + q
    
    return sn

def metodo_b(vet_n, num_vetor):
    seq = []
    num = 1
    for i in range(num_vetor):
        seq.append(num)
        num = num + (i+1)
    
    for j in range(num_vetor):
        vet_n[j] = vet_n[j] + seq[j]

    soma_d = 0
    sn = 0
    for p in vet_n:
        soma_d = p % 10 + ((p//10) % 10)
        sn = sn + soma_d
    
    return sn

def descobrir_mes_final(mes_final_data_invasao):
    if mes_final_data_invasao == 1:
        return "janeiro"
    elif mes_final_data_invasao == 2:
        return "fevereiro"
    elif mes_final_data_invasao == 3:
        return "março"
    elif mes_final_data_invasao == 4:
        return "abril"
    elif mes_final_data_invasao == 5:
        return "maio"
    elif mes_final_data_invasao == 6:
        return "junho"
    elif mes_final_data_invasao == 7:
        return "julho"
    elif mes_final_data_invasao == 8:
        return "agosto"
    elif mes_final_data_invasao == 9:
        return "setembro"
    elif mes_final_data_invasao == 10:
        return "outubro"
    elif mes_final_data_invasao == 11:
        return "novembro"
    elif mes_final_data_invasao == 12 or mes_final_data_invasao == 0:
        return "dezembro"

    
saida_m = False
m = 0
while saida_m == False:
    m = int(input("m:"))
    if m <= 0 or m >= 6:
        print("Esse dado precisa ser maior que 0 e menor que 6")
    else:
        saida_m = True

saida_n = False
n = 0
while saida_n == False:
    n = int(input("n:"))
    if n <= 0 or n >= 11:
        print("Esse dado precisa ser maior que 0 e menor que 11")
    else:
        saida_n = True

m_numeros = []
for i in range(m):
    saida_m = False
    while saida_m == False:
        entrada_m_numeros = int(input("m[%s]: " %i))
        if entrada_m_numeros <= 0 or entrada_m_numeros >= 500:
            print("Entre 0 e 500")
        else:
            m_numeros.append(entrada_m_numeros)
            saida_m = True

n_numeros = []
for i in range(n):
    entrada_n_numeros = int(input("n[%s]: " %i))
    n_numeros.append(entrada_n_numeros)

metodo = descobrir_método(m_numeros)

met_escolhido = 0
if metodo == "Método A":
    met_escolhido = metodo_a(n_numeros, n)
elif metodo == "Método B":
    met_escolhido = metodo_b(n_numeros, n)


dia_estimado = met_escolhido % 31
mes_estimado = met_escolhido % 12

if dia_estimado == 0:
    dia_final = 31
else:
    dia_final = dia_estimado

mes_final = descobrir_mes_final(mes_estimado)

if mes_final == "fevereiro" and dia_final > 28:
    print("Código corrompido!!!!👽")
elif mes_final == ("abril" or "junho" or "setembro" or "novembro") and dia_final > 30:
    print("Código corrompido!!!!👽")
else:
    print(metodo)
    print("Invasão: %s de %s" % (dia_final, mes_final))