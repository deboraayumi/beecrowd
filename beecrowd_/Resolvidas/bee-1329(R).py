while True:
    a = int(input())
    m = 0
    j = 0
    if(a == 0):
        break
    
    jogos = input().split()
    
    for i in jogos:
        if (i == '0'):
            m += 1
        else:
            j += 1
    print(f"Mary won {m} times and John won {j} times")
            