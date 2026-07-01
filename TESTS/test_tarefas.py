import sys
import os
# Força o Python a olhar para a raiz do projeto (gerenciador-tarefas) primeiro
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tarefas import Tarefa

# Função que testa se uma nova tarefa é criada corretamente
def test_criacao_tarefa():
    # Cria uma tarefa de teste
    tarefa_teste = Tarefa(99, "Estudar testes", "Aprender controle de qualidade")
    
    # Verifica (assert) se as informações estão corretas
    assert tarefa_teste.id_tarefa == 99
    assert tarefa_teste.titulo == "Estudar testes"
    assert tarefa_teste.status == "A Fazer"