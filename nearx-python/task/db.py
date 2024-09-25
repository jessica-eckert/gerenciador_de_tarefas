def ler_tarefas_do_arquivo(caminho_do_arquivo: str):
    tarefas = []
    with open(caminho_do_arquivo, "r") as arquivo:
        for linha in arquivo:
            descricao, concluido = linha.strip().split(";")
            tarefa = {
                "descricao": descricao.strip(),
                "concluido": concluido.strip().lower() == "true"  
            }
            tarefas.append(tarefa) 

    return tarefas  

def escrever_tarefas_no_arquivo(caminho_do_arquivo: str, tarefas: list[dict[str, bool]]):
    with open(caminho_do_arquivo, "w") as arquivo:
        for tarefa in tarefas:
            descricao = tarefa["descricao"]  
            concluido = tarefa["concluido"]

            
            arquivo.write(f"{descricao};{str(concluido)}\n")  

    

