
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="REST ToDo API")
DB = {"todo:1": {"id": "todo:1", "title": "Ship it", "done": False}}

class TodoIn(BaseModel):
    title: str
    done: bool = False

@app.get("/todos/{tid}")
def get_todo(tid: str):
    return DB.get(tid, {})

@app.post("/todos")
def create(todo: TodoIn):
    tid = f"todo:{len(DB)+1}"
    DB[tid] = {"id": tid, **todo.model_dump()}
    return DB[tid]
