from departamento import *
def menu_departamento():
    while True:
        print("\n=================")
        print("Departamento")
        print("=================")
        print("1 - INSERIR")
        print("2 - CONSULTAR DEPARTAMENTO")
        print("3 - DELETAR DEPARTAMENTO")
        print("4 - ATUALIZAR DEPARTAMENTO")
        print("0 - Voltar")

        opcao = input("Escolha: ")
        if opcao == "1":
            inserir_departamento()
        elif opcao == "2":
            listar_departamento()
        elif opcao == "3":
            deletar_departamento()
        elif opcao == "4":
            atualizar_departamento()
        elif opcao == "0":
            break
        else: 
            print("Opção Inválida!")

if __name__=="__main__":
    menu_departamento()