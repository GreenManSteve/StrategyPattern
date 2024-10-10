from importlib import import_module
from inspect import getmembers, isclass, isabstract
from .abs_facade import AbsFacade


class FacadeFacory(object):
    @staticmethod
    def create_module(module_name):
        module = import_module('.' + module_name, __package__)
        classes = getmembers(module, lambda m: (isclass(m) and not isabstract(m) and issubclass(m, AbsFacade)))
        return classes[0][1]()

