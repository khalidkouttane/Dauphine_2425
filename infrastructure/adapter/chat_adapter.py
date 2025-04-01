from domain.port.chat_application_port import ChatApplicationPort
from infrastructure.text_generator.cohere_text_generator import CohereTextGenerator
from infrastructure.historic_repository.in_memory_historic_repository import InMemoryHistoricRepository


class ChatApplicationAdapter(ChatApplicationPort):
    def __init__(self, cohere_api_key: str):
        self.text_generator = CohereTextGenerator(cohere_api_key)
        self.history_repo = InMemoryHistoricRepository()

    def get_generated_text(self, prompt: str) -> str:
        return self.text_generator.generate_text(prompt)

    def get_history(self, limit: int) -> list:
        return self.history_repo.get(limit)

    def save_history(self, history: list) -> None:
        self.history_repo.save(history)
