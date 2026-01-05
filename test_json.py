import json


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