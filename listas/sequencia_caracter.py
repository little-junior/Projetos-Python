seq = input()
ult_caracter = ""
dois_espaços = False

for i in seq:
    if i != ' ' and i != ".":
        print(i)
    else: 
        if i == " " and ult_caracter == " " and dois_espaços is False:
            print(i)
            dois_espaços = True
        else:
            dois_espaços = False
    ult_caracter = i

