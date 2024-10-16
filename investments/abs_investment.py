import abc


class AbsInvestment(metaclass=abc.ABCMeta):
    def __init__(self, amount):
        self._amount = amount
        self._total_amount_plus_interest = 0


    @abc.abstractmethod
    def _calculate_interest(self):
        pass