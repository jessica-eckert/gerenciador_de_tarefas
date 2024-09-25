class GerenciadorTarefas:
    def __init__(self, caminho_do_arquivo):
        self.caminho_do_arquivo = caminho_do_arquivo
        self.tarefas = self.ler_tarefas_do_arquivo()

    def adicionar_tarefa(self, descricao):
        tarefa = {
            "descricao": descricao,
            "concluido": False
        }
        self.tarefas.append(tarefa)
        self.escrever_tarefas_no_arquivo()
        print("\nTarefa adicionada com sucesso!")

    def exibir_tarefas(self):
        if len(self.tarefas) == 0:
            print("\n<<<Nenhuma tarefa>>>")
        else:
            for indice, tarefa in enumerate(self.tarefas):
                status = "concluída" if tarefa["concluido"] else "não concluída"
                print(f"{indice + 1}. {tarefa['descricao']} - {status}")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
            self.escrever_tarefas_no_arquivo()
            print("\nTarefa removida com sucesso!")
        else:
            print("\nNúmero de tarefa inválido!")

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["concluido"] = True
            self.escrever_tarefas_no_arquivo()
            print("\nTarefa concluída com sucesso!")
        else:
            print("\nNúmero de tarefa inválido!")

    def ler_tarefas_do_arquivo(self):
        tarefas = []
        try:
            with open(self.caminho_do_arquivo, "r") as arquivo:
                for linha in arquivo:
                    descricao, concluido = linha.strip().split(";")
                    tarefa = {
                        "descricao": descricao,
                        "concluido": concluido == "True"
                    }
                    tarefas.append(tarefa)
        except FileNotFoundError:
            print("\nArquivo não encontrado, iniciando com lista vazia.")
        return tarefas

    def escrever_tarefas_no_arquivo(self):
        with open(self.caminho_do_arquivo, "w") as arquivo:
            for tarefa in self.tarefas:
                # Aqui removemos a vírgula para garantir que a string seja salva corretamente
                descricao = tarefa["descricao"]
                concluido = tarefa["concluido"]
                arquivo.write(f"{descricao};{concluido}\n")

