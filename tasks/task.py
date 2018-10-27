from abc import ABC, abstractmethod


class Task(ABC):
    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def expected_output(self):
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
