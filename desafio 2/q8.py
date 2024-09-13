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
