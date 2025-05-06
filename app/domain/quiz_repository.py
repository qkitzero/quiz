from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.quiz import Quiz


class QuizRepositoryInterface(ABC):
    @abstractmethod
    def create(self, quiz: Quiz) -> None:
        pass

    @abstractmethod
    def read(self, id: UUID) -> Quiz:
        pass
