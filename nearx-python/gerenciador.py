# Gerenciador de tarefas
from task.operacoes import GerenciadorTarefas

def menu():
    caminho_do_arquivo = "C:/Users/jessi/OneDrive/Área de Trabalho/Python/nearx-python/database/db.txt"

    gerenciador = GerenciadorTarefas(caminho_do_arquivo)

    while True:
        print("\nSeja bem-vindo ao gerenciador de tarefas")
        print("1. Ver todas as tarefas")
        print("2. Adicionar uma tarefa")
        print("3. Remover uma tarefa")
        print("4. Concluir uma tarefa")
        print("5. Sair")

        opcao = input("Escolha sua opção: ")

        if opcao == "1":
            gerenciador.exibir_tarefas()
        elif opcao == "2":
            descricao = input("Descrição da tarefa: ")
            gerenciador.adicionar_tarefa(descricao)
        elif opcao == "3":
            gerenciador.exibir_tarefas()
            indice = int(input("Número da tarefa para remover: ")) - 1
            gerenciador.remover_tarefa(indice)
        elif opcao == "4":
            gerenciador.exibir_tarefas()
            indice = int(input("Número da tarefa para concluir: ")) - 1
            gerenciador.concluir_tarefa(indice)
        elif opcao == "5":
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

menu()

        
        
        
        
        
        
        