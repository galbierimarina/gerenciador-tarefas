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

# Função para CRIAR (Create) uma nova tarefa
def adicionar_tarefa(id_tarefa, titulo, descricao):
    nova_tarefa = Tarefa(id_tarefa, titulo, descricao)
    banco_de_tarefas.append(nova_tarefa)
    print(f"Sucesso: A tarefa '{titulo}' foi adicionada!")

# Função para LER/LISTAR (Read) as tarefas
def listar_tarefas():
    print("\n--- Lista de Tarefas da TechFlow ---")
    if not banco_de_tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
    else:
        for tarefa in banco_de_tarefas:
            print(tarefa)
    print("------------------------------------\n")

# --- Testando o nosso sistema ---
adicionar_tarefa(1, "Configurar repositório", "Criar pastas src e testes")
adicionar_tarefa(2, "Revisar uniformes", "Checar a nova política de vestimenta da equipe")
listar_tarefas()