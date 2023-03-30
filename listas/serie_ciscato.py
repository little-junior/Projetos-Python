sinal = 1
soma = 0

for i in range (1, 11):
    elemento = sinal/i
    print(str(-1)+"/"+str(i) if sinal == -1 else str(1)+"/"+str(i))
    soma = soma + elemento
    sinal = sinal * -1

print(soma)

