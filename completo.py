from conexão import conectar
def listar(conn,cursor):
    conn = conectar()
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tribos")
    
    resultados = cursor.fetchall()
    
    for resultado in resultados:
        print(resultado)
    
    cursor.close()
    
    conn.close()
    
def inserir(nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado,id_tribos):
    conn = conectar()
    cursor = conn.cursor()
    
    sql = 'INSERT INTO tribos (nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado,id_tribos) VALUES (%S,%s,%s,%s,%s,%s)'
    val = (nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado,id_tribos)
    cursor.execute(sql,val)
    conn.commit()
    
    print('Registro inserido com sucesso.')
    
    cursor.close()
    conn.close()
    
def atualizar(nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado,id_tribos):
    conn = conectar()
    cursor = conn.cursor()
    
    sql = 'UPDATE tribos SET nome_tribo = %s WHERE id_tribos = %s'
    val = (nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado,id_tribos)
    cursor.execute(sql,val)
    conn.commit()
    #verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
     print('Nenhum registro atualizado.')
    else: 
     print('Registro atualizado com sucesso.')
    cursor.close()
    conn.close()
    
def deletar(id_tribos):
    conn = conectar()
    cursor = conn.cursor
    sql = 'DELETE FROM tribos WHERE id_tribos = %s'
    val = (id_tribos,)
    cursor.execute(sql,val)
    
    conn.commit()
    
    if cursor.rowcount == 0:
     print('Nenhum registro deletado')
    else:
     print('Registro deletado com sucesso')
    cursor.close()
    conn.close()
    
conn = conectar()
cursor = conn.cursor()
while True:
    print('O que você deseja fazer?')
    print('1- Listar tribos')
    print('2- Inserir nova tribo')
    print('3- Atualizar uma tribo')
    print('4- Deletar uma tribo')
    print('0- Sair')
    opcao = int(input('Digite o número da opção desejada: '))
    
    if opcao == 1:
        listar(conn, cursor)
     
    elif opcao == 2:
        cursor = conn.cursor()
        id_tribos = int(input('Digite o id da tribo'))
        nome_tribo = input('Digite o nome da tribo: ')
        num_habitantes = input('Digite o número de habitantes: ')
        renda_mensal = input('Digite a renda média mensal: ')
        escolaridade = input('Digite a escolaridade: ')
        trab_assalariado = input('Possuem trabalho assalariado? (s/n): ')
        inserir(nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado,id_tribos)
        
    elif opcao == 3:
        cursor = conn.cursor()
        id_tribos = int(input('Digite o id da tribo'))
        nome_tribo = input('Digite o nome da tribo: ')
        num_habitantes = input('Digite o número de habitantes: ')
        renda_mensal = input('Digite a renda média mensal: ')
        escolaridade = input('Digite a escolaridade: ')
        trab_assalariado = input('Possuem trabalho assalariado? (s/n): ')
        
        atualizar(nome_tribo, num_habitantes, renda_mensal, escolaridade, trab_assalariado,id_tribos)
    
    elif opcao == 4:
        id_tribos = int(input('Digite o nome da tribo que deseja deletar: '))
        deletar(id_tribos)
        
    elif opcao == 0:
        break
    
    else:
        print('Opção inválida, digite novamente.')

cursor.close()
conn.close()
