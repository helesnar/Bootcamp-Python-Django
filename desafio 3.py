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


'''3. Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''
carrinho = {'água': 5, 'queijo': 3, 'hamburguer': 4, 'pão': 2}
soma = 0
for i in carrinho:
    soma += carrinho[i]
print(f'Você tem {soma} itens no seu carrinho.')


'''4. Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome
'''
dic = {'helena': '99999-9999', 'valma': '98798-7987', 'guilherme': '95555-4444'}
busca = input('Quem deseja buscar na lista telefônica? ')
if busca not in dic:
    sn = input('Esse contato não se encontra na lista. Deseja adicioná-lo? Digite S para sim e N para não: ')
    if sn == 'N':
        print('Consulta finalizada.')
    else:
        num = input(f'Insira o número de contato para {busca}: ')
        dic[busca] = num
else:
    print(f'O telefone de {busca} é {dic[busca]}.')


'''5. Crie duas tuplas. Concatene-as para formar uma nova tupla'''
t1 = (1,2,3,4,5)
t2 = (6, 7, 8, 9, 10)
t3 = t1 + t2
print(t1, t2, t3)


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
