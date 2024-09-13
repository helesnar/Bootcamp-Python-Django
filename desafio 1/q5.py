"""5. Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
"""
bruto =float(input('Insira seu salário bruto, usando "." no lugar de ",": '))
if bruto <= 1903.98:
    ir = 0
    print("Seu salário é isento de imposto de renda")
elif 1903.99 <= bruto <= 2826.65:
    ir = bruto*7.5/100
elif 2826.66 <= bruto <= 3751.05:
    ir = bruto*15/100
elif 3751.06 <= bruto <= 4664.68:
    ir = bruto*22.5/100
else:
    ir = bruto*27.5/100
liq = bruto - ir
print(f"Seu salário líquido é R${liq:.2f} e seu desconto de IR é R${ir:.2f}.")
