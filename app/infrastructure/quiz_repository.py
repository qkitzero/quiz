from uuid import UUID

from sqlalchemy.orm import Session

from app.domain.quiz import Quiz
from app.domain.quiz_repository import QuizRepositoryInterface
from app.infrastructure.quiz_table import QuizTable


class QuizRepository(QuizRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def create(self, quiz: Quiz) -> None:
        quiz_table = QuizTable(id=quiz.id, title=quiz.title)
        self.session.add(quiz_table)
        self.session.commit()

    def read(self, id: UUID) -> Quiz:
        quiz_table = self.session.query(QuizTable).filter_by(id=id).first()
        return Quiz(quiz_table.id, quiz_table.title)
