from abc import ABC, abstractmethod


class Animal(ABC):
    def move(self):
        pass


class Horse(Animal):
    # def move(self):
    #   print("running")
    pass


class Cockroach(Animal):
    def move(self):
        print("crawling")


class Human(Animal):
    def move(self):
        print("walking")


c = Cockroach()
c.move()
h = Horse()
