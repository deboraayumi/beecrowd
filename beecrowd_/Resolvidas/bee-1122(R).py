while True:
    a, b = map(str, input().split())
    if(a == "0" and b == "0"):
        break
    novaString = b.replace(a,"")
    if(novaString == ""):
        print(0)
    else:
        print(int(novaString))


   



