altura = float(input("Digite a altura (m): "))
peso = float(input("Digite o peso (kg): "))

imc = peso / (altura ** 2)

print(f"IMC = {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
