#!/usr/bin/python3

a = int(input('Número A: '))
b = int(input('Número B: '))
c = int(input('Número C: '))

if(a > b and a > c):
    maior = a
if(b > a and b > c):
    maior = b
if(c > b and c > a):
    maior = c

if(a < b and a < c):
    menor = a
if(b < a and b < c):
    menor = b
if(c < b and c < a):
    menor = c



print('Maior número: ' + str(maior))
print('Menor número: ' + str(menor))
