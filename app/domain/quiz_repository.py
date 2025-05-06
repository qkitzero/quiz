from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.domain.quiz import Quiz


class QuizRepositoryInterface(ABC):
    @abstractmethod
    def create(self, quiz: Quiz) -> None:
        pass

    @abstractmethod
    def read(self, id: UUID) -> Quiz:
        pass

    @abstractmethod
    def get_all(self) -> List[Quiz]:
        pass
