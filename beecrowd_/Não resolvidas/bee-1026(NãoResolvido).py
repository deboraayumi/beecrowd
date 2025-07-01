#decimal<->binario
valor = input().split()
a = int(valor[0])
b = int(valor[1])

n1 = [0]*32 
n2 = [0]*32
result_vetor = [0]*32
result = 0


for i in range(1, 33):
    mod_a = a%2
    a = a//2
    if (mod_a == 0):
        n1[-i] = 0
    else:
        n1[-i] = 1

    mod_b = b%2    
    b = b//2
    if (mod_b == 0):
        n2[-i] = 0
    else:
        n2[-i] = 1
    
    if (n1[-i] == n2[-i]):
        result_vetor[-i] = 0
    else:
        result_vetor[-i] = 1



i = 0 
cont =0
soma = 0
print(result_vetor)

for j in range(31,-1,-1):
    print("valor for :",j)
    print(cont,"valor a ser elevado :",31-j)
    print("posição: ",j)
    print("valor que irá ser elevado: ",result_vetor[j])
    novoValor = result_vetor[j] * 2 ** (31-j)
    print("resultado : ",result_vetor[j])
    result += novoValor
    cont+=1
print(result_vetor)



print("\n")
print(result)
print(*n1)
print(*n2)





# 4294967295 4294967295 → 0
# 1234567890 987654321 → 1932735283 result → 01110011010010000110101001100011
# 2147483648 2147483648 → 0
# 305419896 2596069104 → 2290649224
# 0 4294967295 → 4294967295
# 4294967295 0 → 4294967295
# 2863311530 1431655765 → 4294967295
# 305419896 1431655765 → 1581205877
# 1 2 → 3
# 256 512 → 768

# 4 6	2
# 1234567890 987654321	1934125667 
# 2147483648 2147483648	0
# 305419896 2596069104	2290649224
# 0 4294967295	4294967295
# 4294967295 0	4294967295
# 2863311530 1431655765	4294967295
# 305419896 1431655765	158120587   1197540141
# 1 2	3
# 256 512	768