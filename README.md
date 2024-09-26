# Gerenciador de Tarefas

Este projeto é um **gerenciador de tarefas** simples escrito em Python, permitindo a adição, visualização, conclusão e remoção de tarefas de uma lista. As tarefas são armazenadas em um arquivo de texto para garantir que persistam mesmo após o encerramento do programa.

## Funcionalidades

- Adicionar novas tarefas
- Exibir todas as tarefas (com status de conclusão)
- Remover tarefas
- Marcar tarefas como concluídas
- Persistir as tarefas em um arquivo de texto (`db.txt`)

## Estrutura do Projeto
gerenciador_de_tarefas/ │ ├── gerenciador.py # Arquivo principal que inicializa o programa │ ├── task/ # Diretório com funcionalidades para gerenciar tarefas │ ├── init.py # Torna a pasta um módulo Python │ └── operacoes.py # Define a classe GerenciadorTarefas (operações do sistema) │ ├── database/ # Diretório com o banco de dados simples │ ├── init.py # Torna a pasta um módulo Python │ └── db.txt # Armazena as tarefas persistentes │ └── README.md # Documentação do projeto


## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/jessica-eckert/gerenciador_de_tarefas.git
   cd gerenciador_de_tarefas
   
2.Execute o arquivo principal: Certifique-se de que você tenha o Python 3 instalado em sua máquina. 

No terminal, rode:
python gerenciador.py

3.Gerencie suas tarefas: Siga as opções apresentadas no menu interativo do terminal para adicionar, remover, listar ou concluir tarefas.

## Requisitos
Python 3.x

## Exemplo de Uso
Ao executar o programa, você verá o seguinte menu:
Seja bem vindo ao gerenciador de tarefas
1. Ver todas as tarefas
2. Adicionar uma tarefa
3. Remover uma tarefa
4. Concluir uma tarefa
5. Sair

## Contribuição
Para contribuir com este projeto:

1.Faça um fork do projeto. 

2.Crie uma nova branch para suas alterações: git checkout -b minha-nova-feature.

3.Commit suas mudanças: git commit -m 'Adicionei uma nova feature'.

4.Faça o push para a branch: git push origin minha-nova-feature.

5.Abra um Pull Request para revisão.

