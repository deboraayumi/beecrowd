while True:
    try: 
        b = input()
        qtd = 0
        cond = True
        for i in b:
            if("(" == i):
              qtd +=1  
            elif(")" == i):
                if(qtd<1):
                  cond = False
                  break
                else:
                    qtd-=1
                    
        if(cond and qtd == 0):
            print("correct")
        else:
            print("incorrect")
    except EOFError as e:
        break