""" 9. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
"""
horas = int(input('Quantas horas de exercício você costuma fazer na semana? '))
min = horas * 60
cal = min*5*4 #minutos de exercicio * meda de calorias * 4 semanas em um mês
print(f'Se exercitando {horas} horas por semana, você queima, em média {cal} calorias por mês')
