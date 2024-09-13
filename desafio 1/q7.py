"""7. Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
"""
m = float(input('Insira sua altura em metros, usando "." no lugar de ",": '))
kg = float(input('Insira seu peso em kg, usando "." no lugar de ",": '))
imc = kg /(m*m)
print(f'Seu índice de massa corporal (IMC) é {imc:.1f}.')
