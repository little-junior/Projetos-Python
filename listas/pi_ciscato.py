n = int(input())
sinal = -1
pi = 0

if n % 2 == 0:
    n = n - 1

for i in range (1, n + 1, 2):
    sinal = sinal * -1
    pi = pi + sinal * (4/i)

print(pi)