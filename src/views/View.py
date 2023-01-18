import abc

class View(metaclass = abc.ABCMeta):

    """
    Classe générique abstraite , permet la bonne cohésion de toutes les View de chaque Controller.s
    """

    @abc.abstractmethod
    def _makeFrame(self):
        return

    @abc.abstractmethod
    def main(self):
        return

    @abc.abstractmethod
    def close(self):
        return
