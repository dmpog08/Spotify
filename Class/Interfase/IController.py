from abc import ABC, abstractmethod


class IController(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass