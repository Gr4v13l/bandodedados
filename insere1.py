from conexao1 import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
id_animal = int(input('Digite o código do animal: '))
raca = input('Digite a raca do animal: ')
quantidade = input('Digite a quantidade de animais: ')
area = input('Digite onde é encontrado: ')
risco_extincao = input('Possuem risco de extinção? (s/n): ')


sql = 'INSERT INTO animal (id_animal, raca, quantidade, area, risco_extincao) VALUES (%S,%s,%s,%s,%s,%s)'
val = (id_animal, raca, quantidade, area, risco_extincao)
cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount , 'registro(s) inserido(s) com sucesso.')

conn.close()