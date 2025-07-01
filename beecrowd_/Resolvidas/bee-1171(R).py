a = int(input())
numeros = {}
    
for i in range(a):
    b = int(input())
    if(b in numeros):
        numeros[b] +=1
    else:
        numeros[b] = 1
for num in sorted(numeros):
   print(f"{num} aparece {numeros[num]} vez(es)")

# jaFeito = [0]*a

# for i in range(a):
#     b = int(input())
#     numeros[i] = b
# numeros.sort()

# for i in range(a):
#     qtd = 0
#     if(numeros[i] not in jaFeito):
#         for j in range(a):           
#             if(numeros[i] == numeros[j]):
#                 qtd +=1
#                 jaFeito.append(numeros[i])
                
#         print(f"{numeros[i]} aparece {qtd} vez(es)")