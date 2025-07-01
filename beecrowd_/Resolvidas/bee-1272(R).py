a = int(input())

for i in range(a):
    text = input().split(" ")
    novoTexto = ""
    for j in text:
        if(j != ""):
            novoTexto+=j[0]
        
    print(novoTexto)
    

