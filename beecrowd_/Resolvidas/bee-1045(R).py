a,b,c = sorted(map(float,input().split()),reverse = True)
print(a,b,c)
# valores = sorted([a, b, c], reverse=True)
# a, b, c = valores

if (a>=(b+c)):
    print("NAO FORMA TRIANGULO")
elif (a**2 == (b**2+c**2)):
    print("TRIANGULO RETANGULO")
elif (a**2 > (b**2 + c**2)):
    print("TRIANGULO OBTUSANGULO")
elif (a**2 < (b**2 + c**2)):
    print("TRIANGULO ACUTANGULO")
    
if (a==b or b==c):
    print("TRIANGULO ISOSCELES")
elif (a==b and b==c and a==c):
    print("TRIANGULO EQUILATERO")