# from app import VeryImportantClass, decorator # noqa
import types
from collections.abc import Container


def decorator(func):
    def wrapper(*args, **kwargs):
        print('Wrapped')
        return func(*args, **kwargs)
    return wrapper


class VeryImportantClass:

    def __init__(self):
        self.a = 1
        self._b = 0.1
        self._c = 'c'
        self.lst = [1, 2, 3]
        self.dct = {'a': 1, 'b': 2}

    def get_a(self):
        print(self.a)


class HackedClass(VeryImportantClass):

    def __getattribute__(self, item):
        value = super().__getattribute__(item)
        if item.startswith('_'):
            return value
        if isinstance(value, (float, int, complex)):
            return value * 2
        elif isinstance(value, Container):
            return type(value)()
        return value


for attr in dir(VeryImportantClass):
    if attr.startswith('_'):
        continue
    attr_obj = getattr(HackedClass, attr)
    if type(attr_obj) is types.FunctionType:
        setattr(HackedClass, attr, decorator(attr_obj))


def main():
    hc = HackedClass()
    print(hc.a, hc._b, hc._c, hc.lst, hc.dct)


if __name__ == '__main__':
    main()
