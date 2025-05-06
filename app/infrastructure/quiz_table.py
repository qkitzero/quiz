from sqlalchemy import Column, String, Uuid

from app.core.base import Base


class QuizTable(Base):
    __tablename__ = "quiz"

    id = Column("id", Uuid, primary_key=True)
    title = Column("title", String(255), nullable=False)
