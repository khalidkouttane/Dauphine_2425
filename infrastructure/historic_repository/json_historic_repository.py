import os
import json
from domain.port.historic_repository_port import HistoricRepositoryPort


class JsonHistoricRepository(HistoricRepositoryPort):
    def __init__(self, json_path: str):
        self.path = json_path

        # Crée un fichier vide s'il n'existe pas
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump([], f)

    def get(self, limit: int) -> list:
        with open(self.path, 'r') as f:
            history = json.load(f)
        return history[-limit:]

    def save(self, history: list) -> None:
        with open(self.path, 'w') as f:
            json.dump(history, f, indent=2)
