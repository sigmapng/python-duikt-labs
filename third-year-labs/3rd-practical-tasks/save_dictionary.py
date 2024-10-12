from abc import ABC, abstractmethod


class SaveDictionary(ABC):

    @abstractmethod
    def save(self, data, file_path):
        pass
