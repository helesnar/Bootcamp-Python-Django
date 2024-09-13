'''6. Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas
'''
nome = input('Qual é o seu nome? ')
nomeM = nome.upper()
novo = []
for i in nomeM:
    novo.append(i)
novo = novo[::-1]
novo = ''.join(novo)
print(f'{nome}, seu nome ao contrário e em maiúsculas fica {novo}.')
