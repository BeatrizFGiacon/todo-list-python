import json

def filtrar_por_status(lista_tarefas, status_desejado):
    nova_lista = []
    for task in lista_tarefas:
        if task["concluida"] == status_desejado:
            nova_lista.append(task["titulo"].upper())
    return nova_lista

# Criação de nova tarefa
def adicionar_tarefa(lista_tarefas, titulo_novo):
    novoID = len(lista_tarefas) + 1
    novaTarefa = {
        "id": novoID,
        "titulo": titulo_novo,
        "concluida": False
    }
    lista_tarefas.append(novaTarefa)
    return lista_tarefas

# Mudar status da tarefa
def concluir_tarefa(lista_tarefas, id_para_concluir):
    for task in lista_tarefas:
        if task["id"] == id_para_concluir:
            task["concluida"] = True
            break

# Remoção de tarefa
def remover_tarefa(lista_tarefas, id_para_remover):
    nova_lista = []
    for task in lista_tarefas:
        if task["id"] != id_para_remover:
            nova_lista.append(task)
    return nova_lista

def carregarDados():
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
    
    return tarefas

def salvarDados(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def menu():
    tarefas = carregarDados()
    
    while True:
        print("\n=== TO DO LIST ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas Pendentes")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Qual o nome da tarefa? ")
            adicionar_tarefa(tarefas, titulo)
            salvarDados(tarefas)
            print("Tarefa adicionada!")

        elif opcao == "2":
            print("\n--- Pendentes ---")
            pendentes = filtrar_por_status(tarefas, False) 
            
            if len(pendentes) == 0:
                print("Nenhuma tarefa pendente.")
            else:
                for tarefa in pendentes:
                    print(f"- {tarefa}") 

        elif opcao == "3":
            id_user = int(input("Qual ID deseja concluir? "))
            concluir_tarefa(tarefas, id_user)
            salvarDados(tarefas)
            print("Tarefa concluída!")

        elif opcao == "4":
            id_user = int(input("Qual ID deseja remover? "))
            tarefas = remover_tarefa(tarefas, id_user)
            salvarDados(tarefas)
            print("Tarefa removida!")

        elif opcao == "0":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida")

menu()