mes = int(input("Digite um número de 1 a 12: "))

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

if 1 <= mes <= 12:
    print("Mês:", meses[mes - 1])
else:
    print("Número inválido")
    