a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# ordena para garantir que 'hip' seja o maior
lados = sorted([a, b, c])
x, y, hip = lados

if x + y > hip:  # primeiro, verificar se forma triângulo
    if abs(hip**2 - (x**2 + y**2)) < 1e-9:  # tolerância para cálculos float
        print("É um triângulo retângulo")
    else:
        print("Não é um triângulo retângulo")
else:
    print("Não forma um triângulo")

