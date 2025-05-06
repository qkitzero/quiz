from fastapi import FastAPI

from app.interface import health_handler, quiz_handler

app = FastAPI()
app.include_router(health_handler.router)
app.include_router(quiz_handler.router)
