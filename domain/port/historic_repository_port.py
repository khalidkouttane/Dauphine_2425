from abc import ABC, abstractmethod
from typing import List


class HistoricRepositoryPort(ABC):

    @abstractmethod
    def get(self, limit: int) -> List[str]:
        pass

    @abstractmethod
    def save(self, history: List[str]) -> None:
        pass
