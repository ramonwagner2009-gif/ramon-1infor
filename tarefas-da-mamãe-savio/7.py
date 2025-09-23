limite = 50
valor_multa = 4.00
peso = float(input("Digite o peso de peixes (kg): "))
if peso > limite:
    excesso = peso - limite
    multa = excesso * valor_multa
else:
    excesso = 0
    multa = 0
print(f"Peso informado: {peso:.2f} kg")
print(f"Excesso: {excesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")