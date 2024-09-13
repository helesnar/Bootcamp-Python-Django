'''2. Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.
'''
notas = []
aprovados = 0
ord = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
for i in ord:
    soma = 0
    print(f'Insira a seguir as 4 notas do {i} aluno: ')
    for j in range(4):
        n = int(input('Nota do aluno: '))
        soma += n
    media = soma/4
    if media >=7:
        aprovados += 1
    notas.append(media)
print(f'As médias das notas dos alunos foram: {notas} e {aprovados} alunos ficaram com a média maior ou igual a 7.0.')
