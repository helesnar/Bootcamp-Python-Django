"""5. Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
"""
l1 = int(input("Insira um lado do triângulo - "))
l2 = int(input("Insira outro lado do triângulo - "))
l3 = int(input("Insira o último lado do triângulo - "))
if l1 == l2 == l3:
    tipo = "equilátero"
elif l1 != l2 != l3:
    tipo = "escaleno"
else:
    tipo = "isísceles"
print(f"O triângulo de lados {l1}, {l2}, e {l3} é {tipo}.")
