"""6. Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
"""
km = int(input("Insira o tempo total de sua viagem, em km: "))
aviao = km/600
carro = km/100
onibus = km/80
print(f'A sua viagem demoraria {onibus:.1f} horas de ônibus, {carro:.1f} horas de carro ou {aviao:.1f} horas de avião')
