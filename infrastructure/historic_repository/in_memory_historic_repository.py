from domain.port.historic_repository_port import HistoricRepositoryPort


class InMemoryHistoricRepository(HistoricRepositoryPort):
    def __init__(self):
        self._messages = []

    def get(self, limit: int) -> list:
        return self._messages[-limit:]

    def save(self, history: list) -> None:
        self._messages = history
