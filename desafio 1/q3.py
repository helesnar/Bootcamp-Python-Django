"""3. Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
"""
km = int(input("Insira um valor em quilômetros: "))
m = km * 1000
cm = m * 100
mm = cm * 10
print(f'{km} quilômetros equivale a {m} metros, ou {cm} centímetros, ou {mm} milímetros.')
