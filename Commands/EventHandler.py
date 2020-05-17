from abc import ABCMeta, abstractmethod


class EventHandler():
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, message):
        pass

    @abstractmethod
    def can_handle(self, message):
       pass