x = float(input())

sinal = -1
cos = 1
n = int(input())

for i in range (2, n + 1, +2):
    fatorial = 1
    for j in range(1, i):
        fatorial = fatorial * (j + 1)
    cos = cos + sinal * ((x ** i) / fatorial)
    sinal = -sinal

print(cos)

