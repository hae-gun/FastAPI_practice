from select import select
from typing import List

from fastapi import FastAPI, Body, HTTPException, Depends
from database.connection import get_db
from database.orm import ToDo
from database.repository import get_todos, get_todo_by_todo_id
from schema.response import ListToDoResponse, ToDoSchema
from vo.vo import CreateTodoRequest
from sqlalchemy.orm import Session

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


@app.post("/todos", status_code=201)
def create_todo_handler(request: CreateTodoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]


@app.get("/todos", status_code=200)
def get_todos_handler(
        order: str | None = None,
        session: Session = Depends(get_db),
) -> ListToDoResponse:  # | None = None > 스웨거 Required 해제.
    todos: List[ToDo] = get_todos(session=session)
    if order and order == "DESC":
        return ListToDoResponse(
            todos=[ToDoSchema.from_orm(todo) for todo in todos[::-1]]
        )
    return ListToDoResponse(
        todos=[ToDoSchema.from_orm(todo) for todo in todos]
    )


@app.get("/todo/{todo_id}", status_code=200)
def get_todo_handler(
        todo_id: int,
        session: Session = Depends(get_db),
) -> ToDoSchema:
    todo: ToDo | None = get_todo_by_todo_id(session=session, todo_id=todo_id)
    if todo:
        return ToDoSchema.from_orm(todo)
    raise HTTPException(status_code=404, detail="ToDo Not Found")


@app.patch("/todos/{todo_id}", status_code=201)
def update_todo_handler(
        todo_id: int,
        is_done: bool = Body(..., embed=True),
):
    todo = todo_data.get(todo_id)
    if todo:
        todo["is_done"] = is_done
        return todo
    raise HTTPException(status_code=404, detail="ToDo Not Found")


@app.delete("/todo/{too_did}", status_code=204)
def delete_todo_handler(todo_id: int):
    todo = todo_data.pop(todo_id, None)
    if todo:
        return
    raise HTTPException(status_code=404, detail="ToDo Not Found")


