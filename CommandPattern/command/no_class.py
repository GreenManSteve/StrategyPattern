from command.abs_command import AbsCommand


class Noclass(AbsCommand):
    def __init__(self, args):
        self._command = args[0]

    def execute(self):
        print("No command for {}".format(self._command))