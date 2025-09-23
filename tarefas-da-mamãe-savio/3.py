profissao = input("Digite a profissão: ")
valor_hora = float(input("Digite o valor pago por hora: "))
horas_semana = 44
salario_mensal = valor_hora * horas_semana * 4
print(f"O salário mensal do(a) {profissao} é R$ {salario_mensal:.2f}.")
