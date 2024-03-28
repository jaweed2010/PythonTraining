from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    @abstractmethod
    def display_info(self):
        pass
