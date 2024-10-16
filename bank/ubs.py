class UBS(object):
    def __init__(self, product):
        self._product = product

    @property
    def getYearlyCompound(self):
        return self._product.getCompoundAmount