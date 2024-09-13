'''1. Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente""
'''
print('Responda S para sim e N para não.')
perguntas = ["Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","Já trabalhou com a vítima? "]
respostas = []
sim = 0
for i in perguntas:
    r = input(i)
    if r == 'S':
        sim += 1
if sim == 2:
    status = 'Suspeito'
elif sim == 3 or sim == 4:
    status = 'Cúmplice'
elif sim == 5:
    status = 'Assassino'
else:
    status = 'Inocente'
print(f'Você respondeu sim para {sim} perguntas, e por isso é considerado {status}.')
