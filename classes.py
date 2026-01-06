import json

class GerenciadorTarefas:

    def __init__(self):
        self.arquivo = "tarefas.json"
        self.tarefas = self.carregarDados() #pega as tarefas da mememoria

    def carregarDados(self):
        try:
            with open(self.arquivo, "r") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []
    
    def salvarDados(self):
        with open(self.arquivo, "w") as arquivo:
            json.dump(self.tarefas, arquivo, indent=4)
    
    def adicionar_tarefa(self, titulo_novo):
        novoID = len(self.tarefas) + 1
        novaTarefa = {
            "id": novoID,
            "titulo": titulo_novo,
            "concluida": False
        }
        self.tarefas.append(novaTarefa) #adiciono a tarefa na lista 
        self.salvarDados() #salvo os dados na memoria
    
    # Mudar status da tarefa
    def concluir_tarefa(self, id_para_concluir):
        for task in self.tarefas:
            if task["id"] == id_para_concluir:
                task["concluida"] = True
                self.salvarDados()
                break

    # Remoção de tarefa
    def remover_tarefa(self, id_para_remover):
        nova_lista = []
        for task in self.tarefas:
            if task["id"] != id_para_remover:
                nova_lista.append(task)
        self.tarefas = nova_lista
        self.salvarDados()

    def filtrar_por_status(self):
        nova_lista = []
        for task in self.tarefas:
            if task["concluida"] == False:
                nova_lista.append(task["titulo"])
        return nova_lista
            
def menu():
    gerenciador = GerenciadorTarefas()

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
            gerenciador.adicionar_tarefa(titulo)
            print("Tarefa adicionada!")

        elif opcao == "2":
            print("\n--- Pendentes ---")
            pendentes = gerenciador.filtrar_por_status() 
            
            if len(pendentes) == 0:
                print("Nenhuma tarefa pendente.")
            else:
                for tarefa in pendentes:
                    print(f"- {tarefa}") 

        elif opcao == "3":
            id_user = int(input("Qual ID deseja concluir? "))
            gerenciador.concluir_tarefa(id_user)
            print("Tarefa concluída!")

        elif opcao == "4":
            id_user = int(input("Qual ID deseja remover? "))
            gerenciador.remover_tarefa(id_user)
            print("Tarefa removida!")

        elif opcao == "0":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()