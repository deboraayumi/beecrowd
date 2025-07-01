while True:
    a = int(input())
    
    if(a == 0):
        break
    incorretos = [""]*a
    acertos = 0
    tempo = 0
    b = 0
    for i in range(a):
        info = input().split() 
        if (info[2] == "incorrect"):
            incorretos.append(info[0])
        else:
             for j in incorretos:
                if(info[0] == j):
                  b +=1
             acertos +=1
             tempo += int(info[1])
    tempo += 20*b
    print(acertos, tempo)    

