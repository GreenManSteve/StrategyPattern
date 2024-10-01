from command.shipping_order import ShippingOrder
from command.patient import Patient
from command.no_class import Noclass


def get_commands():
    commands = (ShippingOrder, Patient)
    return dict([cls.name, cls] for cls in commands)

def parse_commands(commands, args):
    command = commands.setdefault(args[0], Noclass)
    return command(args)

# my_list can be set to "ShippingOrder", "Patient" or an "Uknown"
my_list = ["ShippingOrder"]
my_list.append(2)

commmands = get_commands()

command = parse_commands(commmands, my_list[0:])
command.execute()