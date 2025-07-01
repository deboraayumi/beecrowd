#bee-1046
a, b = map(int, input().split())

if (a == b):
    print("O JOGO DUROU 24 HORA(S)")
else:
    if( a<b):
        c = b-a
        print(f"O JOGO DUROU {c} HORA(S)")
    if(a>b):
        c=a-b
        hr = 24-c
        print(f"O JOGO DUROU {hr} HORA(S)")
        
#bee-1047
a, b, c, d = map(int, input().split())

if (a == b and a == c and a == d and b == c and b == d and c == d):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    n1 = a*60 + b
    n2 = c*60 + d

    if(n1<n2):
        hr = (n2-n1)//60
        n4 = ((n2-n1)/60)-hr
        min = round(n4*60)
        print(f"O JOGO DUROU {hr} HORA(S) E {min} MINUTO(S)")
    if(n1>n2):
        n3=n2-n1
        hr = (n3 + 1440)//60
        n4 = ((n3 + 1440)/60)-hr
        min = round(n4 * 60)
        
        print(f"O JOGO DUROU {hr} HORA(S) E {min} MINUTO(S)")
        