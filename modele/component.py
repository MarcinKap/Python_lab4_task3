from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, comp_id, price, prefix= '  ' ):
        super().__init__()
        self.__id = comp_id
        self.__price = price
        self.__prefix = prefix

    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price

    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix_setter(self, value):
        self.__prefix = value

    @abstractmethod
    def do_operation(self):
        print('\t', end='')


    def get_children(self):
        return []