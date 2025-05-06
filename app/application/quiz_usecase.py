import uuid
from uuid import UUID

from app.domain.quiz import Quiz
from app.infrastructure.quiz_repository import QuizRepository


class QuizUsecase:
    def __init__(self, quiz_repository: QuizRepository):
        self.quiz_repository = quiz_repository

    def create_quiz(self, title: str) -> Quiz:
        id = uuid.uuid4()
        quiz = Quiz(id, title)
        self.quiz_repository.create(quiz)
        return quiz

    def get_quiz(self, id: UUID) -> Quiz:
        quiz = self.quiz_repository.read(id)
        return quiz
