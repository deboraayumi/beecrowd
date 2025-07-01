a = int(input())

for i in range(a):
    num1 = float(input())
    cont = 0

    while num1 > 1:
        num1 = num1*0.5
        cont+=1 
    print(f"{cont} dias")