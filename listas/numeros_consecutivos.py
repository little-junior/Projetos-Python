N = input()
cont = 0
consecutivo = True

for i in range(0, len(N) - 1):
    if int(N[i]) >= int(N[i + 1]):
        consecutivo = False

print(consecutivo)
