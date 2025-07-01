dias = input().split()
dia = int(dias[1])
horas = input()
b = horas.split(":")
dias2 = input().split()
dia2 = int(dias2[1])
horas2 = input()
b2 = horas2.split(":")

segundos_d1 = dia*86400
segundos_h1 = int(b[0])*3600
segundos_m1 = int(b[1])*60
segundosT = segundos_d1+segundos_h1+segundos_m1+int(b[2])
segundos_d2 = dia2*86400
segundos_h2 = int(b2[0])*3600
segundos_m2 = int(b2[1])*60
segundosT2 = segundos_d2 + segundos_h2 + segundos_m2 + int(b2[2])
seguntosTotal = segundosT2 - segundosT

dia = seguntosTotal // 86400
seguntosTotal %= 86400
horas = seguntosTotal // 3600
seguntosTotal %= 3600
minutos = seguntosTotal // 60
seguntosTotal %= 60

print(f"{dia} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{seguntosTotal} segundo(s)")
