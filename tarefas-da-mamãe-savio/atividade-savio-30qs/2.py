char = input("Digite um caractere: ")

if char.isdigit():
    print("É um número.")
elif char.lower() in "aeiou":
    print("É uma vogal.")
elif char.isalpha():
    print("É uma consoante.")
else:
    print("É um símbolo.")
