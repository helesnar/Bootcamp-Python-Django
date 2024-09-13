'''1. Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.
'''
def soma(a, b, c):
    print(f'A soma de {a}, {b} e {c}, é {a+b+c}.')

n1 = int(input('Insira um número - '))
n2 = int(input('Insira outro número - '))
n3 = int(input('Insira mais um número - '))
soma(n1,n2,n3)

'''2. Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721'''
def inverso(n):
    n = str(n)
    inv = int(n[::-1])
    print(f'O inverso de {n} é {inv}')

n = int(input('Insira um número: '))
inverso(n)


'''3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
'''