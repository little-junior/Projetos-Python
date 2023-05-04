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
- RESTO DA DIVISÃO DE SN POR 31 = DIA DA INVASAO (0 DE RESTO = DIA 31)
- DIVISAO INTEIRA DE SN POR 12 = MES DA INVASAO (0 = DEZEMBRO)
"""
def descobrir_método (vet_m):
    sm = 0
    for i in vet_m:
        sm = sm + i

    sd = 0
    for digito in str(sm):
        sd = sd + int(digito)
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
    seq = [1]
    num = 1
    for i in range(0, num_vetor):
        seq.append(seq[i] + num)
        num += 1
    for j in range(0, num_vetor):
        vet_n[j] = vet_n[j] + seq[j]

    soma_d = 0
    sn = 0
    for p in vet_n:
        soma_d = soma_d + p % 10 + ((p//10) % 10)
    sn = sn + soma_d
    
    return sn

def descobrir_mes(mes_data_invasao):
    if mes_data_invasao == 1:
        return "janeiro"
    elif mes_data_invasao == 2:
        return "fevereiro"
    elif mes_data_invasao == 3:
        return "março"
    elif mes_data_invasao == 4:
        return "abril"
    elif mes_data_invasao == 5:
        return "maio"
    elif mes_data_invasao == 6:
        return "junho"
    elif mes_data_invasao == 7:
        return "julho"
    elif mes_data_invasao == 8:
        return "agosto"
    elif mes_data_invasao == 9:
        return "setembro"
    elif mes_data_invasao == 10:
        return "outubro"
    elif mes_data_invasao == 11:
        return "novembro"
    elif mes_data_invasao == 0:
        return "dezembro"

    
saida_m = False
m_numeros = 0
while saida_m == False:
    m_numeros = int(input("m:"))
    if  int(m_numeros) <= 0 or int(m_numeros) >= 6:
        print("Esse dado precisa ser maior que 0 e menor que 6")
    else:
        saida_m = True

saida_n = False
n_numeros = 0
while saida_n == False:
    n_numeros = int(input("n:"))
    if int(n_numeros) <= 0 or int(n_numeros) >= 11:
        print("Esse dado precisa ser maior que 0 e menor que 11")
    else:
        saida_n = True

lista_m = []
for i in range(int(m_numeros)):
    saida_m_numeros = False
    while saida_m_numeros == False:
        numeros_m = int(input(f"m[{i}]: "))
        if numeros_m <= 0 or numeros_m >= 500:
            print("Entre 0 e 500")
        else:
            lista_m.append(numeros_m)
            saida_m_numeros = True

lista_n = []
for i in range(int(n_numeros)):
    numeros_n = int(input(f"n[{i}]: "))
    lista_n.append(numeros_n)

metodo = descobrir_método(lista_m)

met_escolhido = 0
if metodo == "Método A":
    met_escolhido = metodo_a(lista_n, n_numeros)
elif metodo == "Método B":
    met_escolhido = metodo_b(lista_n, n_numeros)


dia_data_invasao = met_escolhido % 31
mes_data_invasao = met_escolhido % 12

if dia_data_invasao == 0:
    dia = 31
else:
    dia = dia_data_invasao

mes = descobrir_mes(mes_data_invasao)

if mes == "fevereiro" and dia > 28:
    print("Código corrompido!!!!👽")
elif mes == ("abril" or "junho" or "setembro" or "novembro") and dia > 30:
    print("Código corrompido!!!!👽")
else:
    print(metodo)
    print(f"Invasão: {dia} de {mes}")