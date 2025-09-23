dia = int(input("Digite um número de 1 a 7: "))

dias_semana = [
    "Domingo", "Segunda-feira", "Terça-feira", 
    "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"
]

if 1 <= dia <= 7:
    print("Dia da semana:", dias_semana[dia - 1])
else:
    print("Número inválido")

