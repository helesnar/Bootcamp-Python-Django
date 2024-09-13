'''4. Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome
'''
dic = {'helena': '99999-9999', 'valma': '98798-7987', 'guilherme': '95555-4444'}
busca = input('Quem deseja buscar na lista telefônica? ')
if busca not in dic:
    sn = input('Esse contato não se encontra na lista. Deseja adicioná-lo? Digite S para sim e N para não: ')
    if sn == 'N':
        print('Consulta finalizada.')
    else:
        num = input(f'Insira o número de contato para {busca}: ')
        dic[busca] = num
else:
    print(f'O telefone de {busca} é {dic[busca]}.')
