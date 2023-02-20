from abc import ABC, abstractmethod

class ModelInterface(ABC):

    def __init__(self, answer_dict: dict) -> None:
        self.model = self._load_model()
        self.answer = answer_dict
        self.label_list = self.__dict_to_list(self.answer)

    @abstractmethod
    def _load_model(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    def __dict_to_list(self, dictoinary: dict):
        return list(dictoinary)
