from domain.port.historic_repository_port import HistoricRepositoryPort


class HistoricService:
    def __init__(self, historic_repository: HistoricRepositoryPort):
        self.historic_repository = historic_repository

    def get_history(self, limit: int = 10) -> list:
        return self.historic_repository.get(limit)

    def save_history(self, history: list) -> None:
        self.historic_repository.save(history)
