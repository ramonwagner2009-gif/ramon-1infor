salario = float(input("Digite o salário: "))

if salario <= 1500:
    novo = salario * 1.20
elif salario <= 3000:
    novo = salario * 1.15
else:
    novo = salario * 1.10

print(f"Novo salário: R$ {novo:.2f}")
