# Classe que representa o modelo de uma Tarefa no sistema
class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao):
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.status = "A Fazer"  # Toda tarefa nova começa com este status

    def __str__(self):
        return f"[{self.id_tarefa}] {self.titulo} - Status: {self.status}"

# Lista que funcionará como o nosso "banco de dados" temporário
banco_de_tarefas = []

print("Sistema de Gerenciamento de Tarefas inicializado com sucesso!")