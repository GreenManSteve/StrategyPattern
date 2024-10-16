from investments.abs_investment import AbsInvestment


class CallAccount(AbsInvestment):
    _rate = 0.08

    def _calculate_interest(self):
        self._total_amount_plus_interest = self._amount + self._amount * self._rate

    @property
    def getCompoundAmount(self):
        self._calculate_interest()
        return self._total_amount_plus_interest

    def __str__(self):
        return 'Call Account'