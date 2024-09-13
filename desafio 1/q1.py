"""1. Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão 
"""
n1 = int(input("Insira um número inteiro: "))
n2 = int(input("Insira outro número inteiro: "))
som = n1 + n2
sub = n1 - n2
mult = n1*n2
div = n1//n2
resto = n1%2
print (f'A soma de {n1} mais {n2} equivale a {som}.')
print (f'A subtração de {n1} menos {n2} equivale a {sub}.')
print (f'A multiplicção de {n1} vezes {n2} equivale a {mult}.')
print (f'A dvisião de {n1} por {n2} equivale a {div} e resto {resto}')
