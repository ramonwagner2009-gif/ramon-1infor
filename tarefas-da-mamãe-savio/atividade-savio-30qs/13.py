num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisível por 3 e por 5")
elif num % 3 == 0:
    print("Divisível por 3")
elif num % 5 == 0:
    print("Divisível por 5")
else:
    print("Não é divisível por 3 nem por 5")
