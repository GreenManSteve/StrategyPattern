import abc


class AbsCarrier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cost_of_shipping(self):
        pass