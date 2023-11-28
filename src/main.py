from fastapi import FastAPI

from api import todo, news

app = FastAPI()
app.include_router(todo.router)
app.include_router(news.router)


@app.get("/")
def health_check_handler():
    return {"ping": "pong"}


