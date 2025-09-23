h1 = int(input("Digite a hora 1: "))
m1 = int(input("Digite os minutos 1: "))

h2 = int(input("Digite a hora 2: "))
m2 = int(input("Digite os minutos 2: "))

if (h1, m1) < (h2, m2):
    print("O primeiro horário acontece antes.")
elif (h2, m2) < (h1, m1):
    print("O segundo horário acontece antes.")
else:
    print("Os dois horários são iguais.")