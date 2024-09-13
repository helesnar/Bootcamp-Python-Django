'''3. Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''
carrinho = {'água': 5, 'queijo': 3, 'hamburguer': 4, 'pão': 2}
soma = 0
for i in carrinho:
    soma += carrinho[i]
print(f'Você tem {soma} itens no seu carrinho.')
