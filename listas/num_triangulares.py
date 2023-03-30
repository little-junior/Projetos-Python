num = int(input())
triangular = False

for i in range(1, num):
    mult = i * (i + 1) * (i + 2)
    if mult == num:
        triangular = True

print(triangular)


