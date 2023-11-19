from fastapi import FastAPI
from vo.vo import CreateTodoRequest

app = FastAPI()


@app.get("/")
def health_check_handler():
    return {"ping": "pong"}


todo_data = {
    1: {
        "id": 1,
        "contents": "실전! hello FastAPI",
        "is_done": True,
    },
    2: {
        "id": 2,
        "contents": "실전! FastAPI",
        "is_done": False,
    },
    3: {
        "id": 3,
        "contents": "실전! FastAPI",
        "is_done": True,
    },
}


@app.get("/todos")
def get_todos_handler(order: str | None = None): # | None = None > 스웨거 Required 해제.
    ret = list(todo_data.values())
    if order == "DESC":
        return ret[::-1]
    return ret


@app.get("/todo/{todo_id}")
def get_one_handler(todo_id: int):
    return todo_data.get(todo_id, {})


@app.post("/todos")
def create_todo_handler(request: CreateTodoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]