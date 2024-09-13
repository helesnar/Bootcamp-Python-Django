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