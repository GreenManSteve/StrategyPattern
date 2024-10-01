from command.abs_command import AbsCommand
from command.abs_order_command import AbsOrderCommand


class ShippingOrder(AbsCommand, AbsOrderCommand):
    name = "ShippingOrder"
    description = "ShippingOrder"

    def __init__(self, args):
        self._quantity = args[1]

    def execute(self):
        print("Quantity is: {}".format(self._quantity))