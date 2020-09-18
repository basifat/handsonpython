from abc import ABC, abstractmethod


class BaseTable(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def retrieve(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass
