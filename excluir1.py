from conexao1 import conectar

conn = conectar()

cursor = conn.cursor()

busca = input('Digite o animal que deseja bsucar: ')

sql = 'SELECT * FROM animal WHERE raca LIKE %s'
val = ('%'+busca+'%',)
cursor.execute(sql,val)

result = cursor.fetchone()
if result:
    raca = result[1]
    nome = result[1]
    confirmacao = input(f"Tem certeza que deseja deletar o animal'{nome}'? (s/n)")
    if confirmacao.lower() == 's':
        sql = 'DELETE FROM animal WHERE raca = %s'
        val = (raca,)
        cursor.execute(sql,val)
        conn.commit()
        print(f"O animal'{nome}'foi deletada com sucesso!")
    else:
        print('Operação cancelada pelo usuário.')
else: 
 print('Não foi encontrado nenhum animal com o nome informado.')

conn.close()