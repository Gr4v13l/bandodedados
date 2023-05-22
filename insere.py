from conexão import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
id_tribos = int(input('Digite o id da tribo'))
nome_tribo = input('Digite o nome da tribo: ')
num_habitantes = input('Digite o número de habitantes: ')
renda_mensal = input('Digite a renda média mensal: ')
escolaridade = input('Digite a escolaridade: ')
trab_assalariado = input('Possuem trabalho assalariado? (s/n): ')


sql = 'INSERT INTO tribos (id_ tribos,nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado) VALUES (%s,%s,%s,%s,%s)'
val = (id_tribos,nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado)
cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount , 'registro(s) inserido(s) com sucesso.')

conn.close()