while True:
    try:
        texto = input()
        novo_texto = ""
        cont = 0
        for carac in texto:
            if(carac != " "):
                if(cont % 2 == 0):
                    novo_texto += carac.upper()
                else:
                    novo_texto += carac.lower()
                cont+=1
            else:
                novo_texto += " "
                    
                    
        print(novo_texto)
    except EOFError as e:
        break
