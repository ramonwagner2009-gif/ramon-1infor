valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Número de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11    # 11% IR
desconto_inss = salario_bruto * 0.08  # 8% INSS
desconto_sindicato = salario_bruto * 0.05  # 5% sindicato
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Valor pago de IR: R$ {desconto_ir:.2f}")
print(f"Valor pago de INSS: R$ {desconto_inss:.2f}")
print(f"Valor pago para Sindicato: R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
