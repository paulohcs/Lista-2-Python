#!/usr/bin/python3

peso = float(input('Digite o peso (Kg) : '))

if(peso > 50):
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print(str(excesso) + ' Kg de excesso')
print('R$ ' + str(float(multa)) + ' de multa')
