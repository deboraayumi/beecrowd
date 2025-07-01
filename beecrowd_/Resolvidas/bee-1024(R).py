qtd = int(input())

for i in range(qtd):
    metadeDescrip = ""
    palavraDescrip =""
    palavra = input()
    for j in palavra:
        crip = ord(j)
        if (65 <= crip <=90 or 97<= crip <= 122):
            descrip = chr(crip+3)
        else:
            descrip = chr(crip)
        palavraDescrip += descrip
   
    palavraInvertida = palavraDescrip[::-1]  


    qtde = int(len(palavraInvertida)/2)

    metade_final = palavraInvertida[qtde:]
    metade_comeco =  palavraInvertida[:qtde]

    for j in metade_final:
            metade_crip = ord(j)
            metade_descrip = chr(metade_crip-1)
            metadeDescrip += metade_descrip
        

    print(metade_comeco + metadeDescrip)


# Texto #3
# abcABC1
# vxpdylY .ph
# vv.xwfxo.fd