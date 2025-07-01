#cultivo de string
while True:
    n1 = int(input())
    if(n1 == 0):
        break

    vetor_string = [""]*n1
    for i in range(n1):
        vetor_string[i] = str(input())

    vetor_string.sort(key=len) 
    qtd = len(vetor_string)
    relacao = {}

    for i in range(qtd):
        relacao[vetor_string[i]] = []
        for j in range(qtd):
            if(i != j and vetor_string[i] in vetor_string[j]):
                relacao[vetor_string[i]].append(vetor_string[j])
        qtd_total = 0
    for i in range(qtd):
        atual = vetor_string[i]
        caminho = [atual]

        while relacao[atual]:
            proxima = relacao[atual][0] 
            caminho.append(proxima)
            atual = proxima


        if(qtd_total < len(caminho)):

            qtd_total = len(caminho)
       

    print(qtd_total)
