positivo = 0
media = 0.0
for i in range(6):
    a = float(input())
    
    if (a>0):
        positivo += 1
        media += a
    
    
media /= positivo
print(f"{positivo} valores positivos")
print(f"{media:.1f}")