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