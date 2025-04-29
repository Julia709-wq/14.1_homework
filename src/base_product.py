from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def sold(cls):
        pass
