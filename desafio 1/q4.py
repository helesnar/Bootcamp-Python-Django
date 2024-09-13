"""4. Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.
"""
litros = int(input("Insira a quantidade de combustívels consumida, em litros: "))
km = int(input('Insira a distância percorrida, em quilômetros: '))
media = km//litros
print(f'O seu consumo médio é de {media}km/l')
