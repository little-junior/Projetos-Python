N = int(input())
cont = 1
cont_2 = 0

for i in range(0, N):
    num = i + cont
    print(f"{num}", end = ", ")
    cont_2 +=1
    cont = cont + cont_2


