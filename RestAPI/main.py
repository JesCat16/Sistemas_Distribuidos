from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tarefas = list()

class Tarefa(BaseModel):
    nome: str
    numero: int


@app.get("/")
def root():
    return tarefas


@app.get("/buscarContato/{nome}")
def get_tarefa(nome: str):
    for n in tarefas:
        if n.nome == nome:
            ind = tarefas.index(n)
            break
    return tarefas[ind]

@app.post("/adicionarContato/")
def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return len(tarefas)

@app.put("/atualizarContato/{nome}")
def marcar_feito(nome: str, numero: int):
    for n in tarefas:
        if n.nome == nome:
            n.numero = numero
            ind = tarefas.index(n)
            break
    return tarefas[ind]

@app.delete("/deletarContato/{nome}")
def deletar_tarefa(nome: str):
    for n in tarefas:
        if n.nome == nome:
            ind = tarefas.index(n)
            break
    tarefa = tarefas.pop(ind)
    return tarefa


