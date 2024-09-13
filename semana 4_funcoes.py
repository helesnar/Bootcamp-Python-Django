#manipulação de arquivos

file = 'arquivo.txt' #não precisa de variavel, podia ser o nome do arquivo
'''leitura = open(file, 'r') #r - read
escrita = open(file, 'w') #w - write
binario = open(file, 'wb') #wb - write binary (?)'''

escrita = open(file, 'w')
escrita.write('Oi estou escrevendo!') #escrevendo
escrita.close() #fechar pra poder abrir de novo depois, pra leitura

leitura = open(file, 'r') #abrir como read pra poder ler
ler = leitura.read() #ler
print(ler)
leitura.close()

#try except
'''evita dar erro!!!!!!!
funciona pra erro. Tente isso! se não, faça as exceções. exemplos:
except ZeroDivisionError:
except TypeError as e:
as e - o "e" é de "error", diz o erro do jeito python.
podemos botar um print com nossas palavras e o {e} com format.
except(ValueError, TypeError): - duas exceções na mesma linha.
pode usar o else! mas no entendi como'''