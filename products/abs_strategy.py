import abc

class AbsProduct(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Shipping_cost(self):
        pass