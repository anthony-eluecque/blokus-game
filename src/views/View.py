import abc


"""
    Responsible for the program interface.
"""
class View(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def main(self):
        return

    @abc.abstractmethod
    def close(self):
        return