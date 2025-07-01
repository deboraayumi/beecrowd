a = float(input())

if (0<=a<=400.00):
    per = 0.15
    reajuste = a*per

elif (400.01 <= a <= 800.00):
    per = 0.12
    reajuste = a*per

elif(800.01 <= a <= 1200.00):
    per = 0.10
    reajuste = a*per

elif(1200.01 <= a <= 2000.00):
    per = 0.07
    reajuste = a*per

elif(a > 2000.00):
    per = 0.04
    reajuste = a*per


print(f"Novo salario: {a+reajuste:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {int(per*100)} %")