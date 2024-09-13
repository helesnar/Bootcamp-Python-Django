"""7. Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
"""
id = int(input("Qual é a sua idade? "))
if id < 14:
    fase = 'criança'
elif id < 20:
    fase = 'adolescente'
elif id < 60:
    fase = 'adulto'
else:
    fase = 'idoso'
print(f'Com {id} anos, você é {fase}.')
