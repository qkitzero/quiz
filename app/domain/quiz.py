from uuid import UUID


class Quiz:
    def __init__(self, id: UUID, title: str):
        self.id = id
        self.title = title
