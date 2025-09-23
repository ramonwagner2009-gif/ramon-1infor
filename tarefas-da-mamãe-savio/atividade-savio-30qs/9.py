a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

dist_a = abs(100 - a)
dist_b = abs(100 - b)

if dist_a < dist_b:
    print(f"{a} está mais próximo de 100")
elif dist_b < dist_a:
    print(f"{b} está mais próximo de 100")
else:
    print("Os dois estão à mesma distância de 100")