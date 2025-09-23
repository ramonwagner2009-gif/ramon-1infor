h1 = int(input("Hora 1: "))
m1 = int(input("Minutos 1: "))
s1 = int(input("Segundos 1: "))

h2 = int(input("Hora 2: "))
m2 = int(input("Minutos 2: "))
s2 = int(input("Segundos 2: "))

t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2

if t1 > t2:
    print("O primeiro horário é maior.")
elif t2 > t1:
    print("O segundo horário é maior.")
else:
    print("Os dois horários são iguais.")
    