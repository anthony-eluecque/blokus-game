from abc import ABCMeta,abstractmethod

class Bouton(metaclass = ABCMeta):

    @abstractmethod
    def _createWidget(self):
        pass

    @abstractmethod
    def _placeWidget(self,x_pos:int,y_pos:int):
        pass

    @abstractmethod
    def main(self):
        pass