class Shipping_Cost(object):
    def __init__(self, prod):
        self._prod = prod

    def get_shipping_cost(self):
        return self._prod.Shipping_cost()
