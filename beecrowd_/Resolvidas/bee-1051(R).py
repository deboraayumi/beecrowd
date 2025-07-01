a = float(input())

if (0<=a<=2000.00):
    print("Isento")
else:

    if (2000.01 <= a <= 3000.00):
        b = a-2000
        impT = b*0.08

    elif(3000.01 <= a <= 4500.00):
        b = a-3000
        imp1 = 80
        imp2 = b*0.18
        impT = imp1 + imp2

    elif(a > 4500.00):
        b = a-4500
        imp1 = 80
        imp2 = 270
        imp3 = b*0.28
        impT = imp1 + imp2 + imp3
        
    print(f"R$ {impT:.2f}")


