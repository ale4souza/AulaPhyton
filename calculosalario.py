valor_horas_trabalhadas = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = float(input('Quantas horas você trabalhou no mês? '))

salario_bruto = valor_horas_trabalhadas*horas_trabalhadas

ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
Salario_liquido = salario_bruto-ir-inss-sindicato

print("+ Salário Bruto : R$", salario_bruto)
print("- IR (11%) : R$", ir)
print("- INSS (8%) : R$", inss)
print("- Sindicato ( 5%) : R$", sindicato)
print("= Salário Liquido : R$", Salario_liquido)
