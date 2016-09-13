#!/usr/bin/python3

a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if((b-c < a and a < b+c) and (a-c < b and b < a+c) and (a-b < c and c < a+b)):
    if(a==b and b==c):
        print('O triângulo é equilátero')
    if((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
        print('O triângulo é isósceles')
    if(a!=b and a!=c and b!=c):
        print('O triângulo é escaleno')
else:
    print('Não forma um triângulo')
