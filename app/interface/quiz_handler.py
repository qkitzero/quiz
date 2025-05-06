from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.quiz_usecase import QuizUsecase
from app.core.db import get_db_session
from app.infrastructure.quiz_repository import QuizRepository

router = APIRouter(prefix="/quiz")


def get_quiz_repository(
    session: Session = Depends(get_db_session),
) -> QuizRepository:
    return QuizRepository(session=session)


def get_quiz_usecase(
    quiz_repository: QuizRepository = Depends(get_quiz_repository),
) -> QuizUsecase:
    return QuizUsecase(quiz_repository=quiz_repository)


@router.post("/")
def create_quiz(title: str, quiz_usecase: QuizUsecase = Depends(get_quiz_usecase)):
    quiz = quiz_usecase.create_quiz(title)
    return {"id": quiz.id, "title": quiz.title}


@router.get("/{id}")
def get_quiz(id: UUID, quiz_usecase: QuizUsecase = Depends(get_quiz_usecase)):
    quiz = quiz_usecase.get_quiz(id)
    return {"title": quiz.title}
