
from cadastro_alunos import GerenciadorAlunos

def main():
    sistema = GerenciadorAlunos()

    while True:
        print("\n--- Sistema de Cadastro de Alunos ---")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Buscar aluno")
        print("4. Calcular média da turma")
        print("5. Atualizar nota")
        print("6. Remover aluno")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar_aluno()
        elif opcao == "2":
            sistema.listar_alunos()
        elif opcao == "3":
            sistema.buscar_aluno()
        elif opcao == "4":
            sistema.calcular_media()
        elif opcao == "5":
            sistema.atualizar_nota()
        elif opcao == "6":
            sistema.remover_aluno()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()