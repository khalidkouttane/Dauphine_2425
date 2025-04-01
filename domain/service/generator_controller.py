from domain.port.generator_controller_port import GeneratorControllerPort
from domain.service.text_generation_service import TextGenerationService
from domain.service.historic_service import HistoricService


class GeneratorControllerAdapter(GeneratorControllerPort):
    
    def __init__(self,
                 text_generation_service: TextGenerationService,
                 historic_service: HistoricService):
        self.text_generation_service = text_generation_service
        self.historic_service = historic_service

    def generate_message(self, prompt: str) -> str:
        history = self.historic_service.get_history(limit=10)
        full_prompt = self._build_prompt(history, prompt)
        response = self.text_generation_service.get_generated_text(full_prompt)
        updated_history = history + [f"Utilisateur : {prompt}", f"Assistant : {response}"]
        self.historic_service.save_history(updated_history)
        return response

    def _build_prompt(self, history: list, current_prompt: str) -> str:
        prompt = "\n".join(history)
        prompt += f"\nUtilisateur : {current_prompt}\nAssistant :"
        return prompt
