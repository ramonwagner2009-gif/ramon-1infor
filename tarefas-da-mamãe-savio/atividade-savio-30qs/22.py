a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if b != 0 and a % b == 0:
    print(f"{a} é múltiplo de {b}")
if a != 0 and b % a == 0:
    print(f"{b} é múltiplo de {a}")
if (b == 0 or a % b != 0) and (a == 0 or b % a != 0):
    print("Nenhum é múltiplo do outro")
    