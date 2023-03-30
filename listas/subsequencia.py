N = int(input("Digite quantos números terá a sequencia: "))
sub = ""

for entrada_nums in range(0, N):
    num = input("Digite o número: ")
    sub = sub + num

cont_sub = ""

for i in sub:
    cont = 0
    for j in sub:
        cont = cont + 1 if j == i else cont + 0
    cont_sub = cont_sub + str(cont)

maior_sub = cont_sub[0]

for z in range(0, N):
    maior_sub = cont_sub[z] if maior_sub < cont_sub[z] else maior_sub

print(maior_sub)
    
    


