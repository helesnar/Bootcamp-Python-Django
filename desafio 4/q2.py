
'''2. Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721'''
def inverso(n):
    n = str(n)
    inv = int(n[::-1])
    print(f'O inverso de {n} é {inv}')

n = int(input('Insira um número: '))
inverso(n)