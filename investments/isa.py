from investments.abs_investment import AbsInvestment


class Isa(AbsInvestment):
    _rate = 0.04

    def _calculate_interest(self):
        self._total_amount_plus_interest = self._amount + self._amount * self._rate

    @property
    def getCompoundAmount(self):
        self._calculate_interest()
        return self._total_amount_plus_interest

    def __str__(self):
        return 'ISA'