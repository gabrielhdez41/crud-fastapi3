from fastapi import FastAPI # type: ignore
from routes.todo import router # type: ignore

app = FastAPI()

app.include_router(router)