from command.abs_command import AbsCommand
from command.abs_order_command import AbsOrderCommand


class Patient(AbsCommand, AbsOrderCommand):
    name = "Patient"
    description = "Patient"

    def __init__(self, args):
        self._quantity = args[1]

    def execute(self):
        print("Patient Requires: {} admission".format(self._quantity))