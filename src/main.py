from fastapi import FastAPI

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