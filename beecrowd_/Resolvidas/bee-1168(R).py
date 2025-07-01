qtd = int(input())
leds = {
    "1":2,
    "2":5,
    "3":5,
    "4":4,
    "5":5,
    "6":6,
    "7":3,
    "8":7,
    "9":6,
    "0":6
 }
for i in range(qtd):
    a = input()
    total = 0
    for j in a:
        if j in leds:
            total += leds[j]

    print(f"{total} leds")