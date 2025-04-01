from abc import ABC, abstractmethod
from typing import List

class ChatApplicationPort(ABC):

    @abstractmethod
    def get_generated_text(self, prompt: str) -> str:
        pass

    @abstractmethod
    def get_history(self, limit: int) -> List[str]:
        pass

    @abstractmethod
    def save_history(self, history: List[str]) -> None:
        pass
