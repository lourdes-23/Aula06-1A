# meu_dic = {'chave' : 'valor'}
alunos = {'Maria':888,'João':777,'Ana':555}
alunos['Maria'] = 444 # atualizar o valor
print(alunos)
alunos['Kiko'] = 222 #adicionar chave e valor
print(alunos)
alunos.pop('João')# remover a chave e valor
for nome, matricula in alunos.items(): # alterando no dicionário
    print(f'matricula {matricula} Nome {nome}')
alunosCopia = alunos.copy()
alunosCopia['Ana'] = 999
print('Dicionario Alunos ',alunos)
print('Dicionario  alunosCopia ',alunosCopia)