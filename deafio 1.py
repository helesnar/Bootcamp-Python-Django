"""1. Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão 
"""
n1 = int(input("Insira um número inteiro: "))
n2 = int(input("Insira outro número inteiro: "))
som = n1 + n2
sub = n1 - n2
mult = n1*n2
div = n1//n2
resto = n1%2
print (f'A soma de {n1} mais {n2} equivale a {som}.')
print (f'A subtração de {n1} menos {n2} equivale a {sub}.')
print (f'A multiplicção de {n1} vezes {n2} equivale a {mult}.')
print (f'A dvisião de {n1} por {n2} equivale a {div} e resto {resto}')


""" 2. Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.
"""
ano = int(input("Insira seu ano de nascimento: "))
idade = 2024 - ano
print(f'Você nasceu em {ano} e atualmente tem {idade} anos.')


"""3. Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
"""
km = int(input("Insira um valor em quilômetros: "))
m = km * 1000
cm = m * 100
mm = cm * 10
print(f'{km} quilômetros equivale a {m} metros, ou {cm} centímetros, ou {mm} milímetros.')


"""4. Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.
"""
litros = int(input("Insira a quantidade de combustívels consumida, em litros: "))
km = int(input('Insira a distância percorrida, em quilômetros: '))
media = km//litros
print(f'O seu consumo médio é de {media}km/l')


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


"""7. Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
"""
m = float(input('Insira sua altura em metros, usando "." no lugar de ",": '))
kg = float(input('Insira seu peso em kg, usando "." no lugar de ",": '))
imc = kg /(m*m)
print(f'Seu índice de massa corporal (IMC) é {imc:.1f}.')

"""8. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
"""
sph = float(input("Quanto você recebe por hora? ")) #salario por hora
hora = int(input('Quantas horas você trabalhou esse mês? '))
total = hora * sph
print(f'Trabalhando {hora} horas por mês e recebendo R${sph:.2f} por hora, você recebeu R${total:.2f} esse mês.')


""" 9. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
"""
horas = int(input('Quantas horas de exercício você costuma fazer na semana? '))
min = horas * 60
cal = min*5*4 #minutos de exercicio * meda de calorias * 4 semanas em um mês
print(f'Se exercitando {horas} horas por semana, você queima, em média {cal} calorias por mês')


'''10. Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
Lembrando que para o retorno vamos usar print com as variáveis
criadas e este texto é somente um exemplo, utilizem a criatividade.'''
nome = input("Nome: ")
idade = int(input('Idade: '))
livro = input("Livro preferido: ")
filme = input("Filme preferido: ")
print(f'Oi, prazer em te conhecer! Meu nome é {nome} e tenho {idade} anos. Falando um pouco mais sobre mim, meu livro favorito é {livro} e meu filme favorito é {filme}. E você?')