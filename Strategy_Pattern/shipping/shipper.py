class Shipper(object):
    def __init__(self, carrier):
        self._carrier = carrier

    def get_cost(self):
        return self._carrier.cost_of_shipping()