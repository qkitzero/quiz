from fastapi import FastAPI

from app.interface import quiz_handler

app = FastAPI()
app.include_router(quiz_handler.router)
