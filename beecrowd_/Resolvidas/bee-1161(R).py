import math
while True:
    try:
        a, b = map(int, input().split())

        resultA = math.factorial(a)
        resultB = math.factorial(b)
        print(resultA+resultB)
    except EOFError as e:
        break