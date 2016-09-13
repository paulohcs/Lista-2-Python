#!/usr/bin/python3

import math

area = float(input('Área a ser pintada(m²): '))

latas = math.ceil(area/(3*18))

print('Quantidade de latas: ' + str(latas))
print('Preço total: R$ ' + str(float(latas*80)))
