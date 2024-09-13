"""1. Faça um Programa que peça dois números e imprima o maior deles.
"""
n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
if n1 > n2:
    print(f'O número {n1} é maior que {n2}')
else:
    print(f'O número {n2} é maior que o número {n1}.')


"""2. Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
turno = input("Em qual turno você estuda? Digite M para matutino, V para Vespertino ou N para Noturno. - ")
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")


"""3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
"""
nota = int(input("Insira uma nota de 0 a 10 - "))
while nota<0 or nota>10:
    nota = int(input("Você não digitou um valor válido. Insira uma nota de 0 a 10 - "))
print(f'{nota} é uma nota válida!')


"""4. Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
"""
nota = int(input("Insira sua nota do exame, de 0 a 10 - "))
while nota<0 or nota>10:
    nota = int(input("Você não digitou um valor válido. Insira sua nota do exame, de 0 a 10 - "))
if nota >= 7:
    print("Parabéns! Você foi aprovado!")
else:
    print("Você foi reprovado.")


"""5. Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
"""
l1 = int(input("Insira um lado do triângulo - "))
l2 = int(input("Insira outro lado do triângulo - "))
l3 = int(input("Insira o último lado do triângulo - "))
if l1 == l2 == l3:
    tipo = "equilátero"
elif l1 != l2 != l3:
    tipo = "escaleno"
else:
    tipo = "isísceles"
print(f"O triângulo de lados {l1}, {l2}, e {l3} é {tipo}.")


"""6. Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.
"""
login = input("Login - ")
senha = input("Senha - ")
while login != "admin" or senha != "admin123":
    print("Acesso negado. Login ou senha incorretos. Tente novamente.")  
    login = input("Login - ")
    senha = input("Senha - ")
print("Acesso permitido. Bem-vindo.")


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


"""8. Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.
"""
n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
n3 = int(input("Insira um terceiro número: "))
if n1>=n2 and n1>=n3:
    maior = n1
elif n2>=n1 and n2>=n3:
    maior = n2
else:
    maior = n3    
print(f'{maior} é o maior número dentre os três.')


"""9. O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
"""
n = int(input("Insira um número - "))
par, impar = 0, 0 
while n!= 0:
    if n>0 and n%2 == 0:
        par += 1
    elif n > 0 and n%2 == 1:
        impar += 1
    n = int(input("Insira um número - "))
print(f"Você inseriu o número zero. No total, foram inseridos {impar} números ímpares e {par} números pares positivos.")


'''10. Faça um programa que lê três números inteiros e os mostra em ordem
crescente.
'''
n1 = int(input("Insira um número: "))
maior, menor = n1, n1
n2 = int(input("Insira outro número: "))
n3 = int(input("Insira um terceiro número: "))
for i in [n2,n3]:
    if i>=maior:
        maior = i
    elif i<=menor:
        menor = i
for i in [n1,n2,n3]:
    if i != maior and i != menor:
        meio = i
print(f'Ordem crescente: {menor}, {meio}, {maior}')