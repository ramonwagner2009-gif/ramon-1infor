num = int(input("Digite um número inteiro de 3 dígitos: "))

if 100 <= num <= 999:
    if str(num) == str(num)[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
else:
    print("Número inválido, precisa ter 3 dígitos")
    