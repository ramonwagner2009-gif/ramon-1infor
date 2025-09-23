nota = float(input("Digite a nota (0 a 10): "))

if 9 <= nota <= 10:
    print("Conceito A")
elif 7 <= nota < 9:
    print("Conceito B")
elif 5 <= nota < 7:
    print("Conceito C")
elif 0 <= nota < 5:
    print("Conceito D")
else:
    print("Nota inválida")

