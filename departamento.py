from banco import conectar

def inserir_departamento():
    nome = input("Digite o nome do departamento: ")
    conexao = conectar ()
    cursor = conexao.cursor()

    sql = """
            INSERT INTO departamentos(nome)
            VALUES (%s)
        """
    cursor.execute(sql, (nome,))
    conexao.commit()
    cursor.close()
    print("Departamento inserido com sucesso!")

def listar_departamento():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
            SELECT id, nome FROM departamentos ORDER BY id
        """
    cursor.execute(sql)
    departamentos = cursor.fetchall()

    print("\n=================")
    print("Departamentos")
    print("=================")

    if not departamentos:
        print("Nenhum departamento cadastrado.")
    else:
        for departamento in departamentos:
            print(
                f"ID:{departamento[0]} | "
                f"Nome:{departamento[1]}  "
            )

    cursor.close()
    conexao.close()

def deletar_departamento():
    listar_departamento()
    id_departamento = input("Digite o ID do departamento que deseja deletar: ")
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM departamentos WHERE id = %s"
    cursor.execute(sql, (int(id_departamento),))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Departamento deletado com sucesso!")

def atualizar_departamento():
    listar_departamento()
    id_departamento = input("Digite o ID do departamento que deseja atualizar: ").strip()
    if not id_departamento.isdigit():
        print("ID inválido.")
        return
    novo_nome = input("Digite o novo nome do departamento: ").strip()
    if not novo_nome:
        print("Nome do departamento não pode estar vazio!")
        return
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "UPDATE departamentos SET nome = %s WHERE id = %s"
    cursor.execute(sql, (novo_nome, int(id_departamento)))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Departamento atualizado com sucesso!")