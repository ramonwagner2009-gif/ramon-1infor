a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a > b:
    print(f"O maior é {a}")
    print("Diferença:", a - b)
elif b > a:
    print(f"O maior é {b}")
    print("Diferença:", b - a)
else:
    print("Os números são iguais (diferença 0).")
    