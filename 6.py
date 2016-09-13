#!/usr/bin/python3

dinheiro = float(input('Dinheiro ganho por hora(R$): '))
horas = int(input('Horas trabalhadas no mês: '))

salarioB = dinheiro*horas

ir = salarioB * 0.11
inss = salarioB * 0.08
sindicato = salarioB * 0.05

salarioL = salarioB - ir - inss - sindicato

print('+ R$ ' + str(salarioB) + '	Salário Bruto')
print('- R$ ' + str(ir) + '	IR(11%)')
print('- R$ ' + str(inss) + '	INSS(8%)')
print('- R$ ' + str(sindicato) + '	Sindicato(5%)')
print('= R$ ' + str(salarioL) + '	Salário Líquido')
