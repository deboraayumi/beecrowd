a = int(input())

for i in range(a):
    b = input()
    new_b = b.replace(".", "")
    qtd = 0
    qtdDima = 0
    for carac in new_b:
        if("<" == carac):
            qtd += 1
        elif(">" == carac):
            if(qtd == 0):
                continue
            else:
                qtdDima+=1
                qtd-=1
    print(qtdDima)
    